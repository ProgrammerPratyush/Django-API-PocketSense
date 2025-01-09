from decimal import Decimal
from django.http import HttpResponse, JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from .expense_analysis import analyze_spending, detect_spending_patterns
from .models import Student, Group, Expense, Category, Settlement, RecurringExpense, ExpenseTag, SavingsGoal
from .openai_service import get_openai_response
from .serializers import StudentSerializer, GroupSerializer, ExpenseSerializer, CategorySerializer, \
    SettlementSerializer, RecurringExpenseSerializer, ExpenseTagSerializer, SavingsGoalSerializer
from .smart_splitting import split_expenses
from .tasks import check_spending_patterns

# Root View
def home(request):
    """
    A simple root view to verify the API is working.
    """
    return HttpResponse("<h1>Welcome to PocketSense API</h1>")

# Custom Pagination Class
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Student ViewSet
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='by-college')
    def filter_by_college(self, request):
        """
        Custom action to filter students by college.
        """
        college_name = request.query_params.get('college', None)
        if not college_name:
            return Response({"error": "College name not provided"}, status=status.HTTP_400_BAD_REQUEST)
        students = self.queryset.filter(college__icontains=college_name)
        serializer = self.get_serializer(students, many=True)
        return Response(serializer.data)

# Group ViewSet
class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'], url_path='members')
    def get_group_members(self, request, pk=None):
        """
        Custom action to retrieve all members of a group.
        """
        group = self.get_object()
        members = group.members.all()
        student_serializer = StudentSerializer(members, many=True)
        return Response(student_serializer.data)

# Expense ViewSet
class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category', None)
        if category:
            queryset = queryset.filter(category__name__icontains=category)
        return queryset

    @action(detail=True, methods=['post'], url_path='split')
    def split_expense(self, request, pk=None):
        expense = self.get_object()
        # You could also pass in additional parameters to the smart splitting function
        result = split_expenses(expense.amount, expense.group.members)
        return Response(result)

    # AI-powered Smart Splitting Endpoint
    @action(detail=True, methods=['get'], url_path='suggest-split')
    def suggest_split_action(self, request, pk=None):
        expense = self.get_object()
        group = expense.group
        # Construct the prompt for OpenAI to suggest an expense split
        prompt = f"Suggest a way to split the expense of {expense.amount} among {len(group.members)} people. Expense details: {expense.description if expense.description else 'No description'}"
        ai_suggestion = get_openai_response(prompt)
        return Response({"suggested_split": ai_suggestion})

    # Anonymous Expense Sharing
    @action(detail=True, methods=['post'], url_path='anonymous-share')
    def anonymous_share(self, request, pk=None):
        expense = self.get_object()
        expense.anonymous = True  # Assuming you added an 'anonymous' field to the Expense model
        expense.save()
        return Response({"message": "Expense shared anonymously!"})

# Category ViewSet
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

# Settlement ViewSet
class SettlementViewSet(ModelViewSet):
    queryset = Settlement.objects.all()
    serializer_class = SettlementSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'], url_path='update-status')
    def update_payment_status(self, request, pk=None):
        """
        Custom action to update the payment status of a settlement.
        """
        settlement = self.get_object()
        settlement.payment_status = request.data.get('payment_status', settlement.payment_status)
        settlement.save()
        return Response({"message": f"Settlement {settlement.id} status updated successfully!"})

# RecurringExpense ViewSet
class RecurringExpenseViewSet(ModelViewSet):
    queryset = RecurringExpense.objects.all()
    serializer_class = RecurringExpenseSerializer
    permission_classes = [IsAuthenticated]

# ExpenseTag ViewSet
class ExpenseTagViewSet(ModelViewSet):
    queryset = ExpenseTag.objects.all()
    serializer_class = ExpenseTagSerializer
    permission_classes = [IsAuthenticated]

# SavingsGoal ViewSet
class SavingsGoalViewSet(ModelViewSet):
    queryset = SavingsGoal.objects.all()
    serializer_class = SavingsGoalSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'], url_path='update-progress')
    def update_progress(self, request, pk=None):
        """
        Update the progress of a savings goal.
        """
        savings_goal = self.get_object()
        saved_amount = Decimal(request.data.get('saved_amount', 0))
        savings_goal.saved_amount += saved_amount
        savings_goal.save()
        return Response({"message": f"Goal {savings_goal.goal_name} updated successfully!"})

# AI Algorithm Functions
@api_view(['GET'])
def calculate_smart_split(request):
    """
    Endpoint to calculate a smart split for expenses among a group of students.
    """
    expenses = [100, 50, 30]  # Example data, you would retrieve from the request in a real scenario
    members = ["student1", "student2", "student3"]  # Example members
    result = split_expenses(expenses, members)
    return JsonResponse(result)

@api_view(['GET'])
def analyze_user_spending(request):
    """
    Endpoint to analyze user spending and generate insights.
    """
    user_expenses = {
        "student1": {"food": 200, "travel": 50},
        "student2": {"food": 150, "entertainment": 100}
    }
    result = analyze_spending(user_expenses)
    return JsonResponse(result)

@api_view(['GET'])
def detect_overspending(request):
    """
    Endpoint to detect overspending by users based on predefined thresholds.
    """
    user_expenses = {
        "student1": {"food": 600, "travel": 150},
        "student2": {"food": 450, "entertainment": 50}
    }
    result = detect_spending_patterns(user_expenses)
    return JsonResponse(result)
