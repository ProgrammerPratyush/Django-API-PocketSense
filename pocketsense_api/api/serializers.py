from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student, Group, Expense, Category, Settlement, RecurringExpense, ExpenseTag, SavingsGoal

# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

# Serializer for the Student model with a nested User representation
class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested user serializer for detailed user information

    class Meta:
        model = Student
        fields = ['id', 'user', 'college', 'semester', 'default_payment_method']

# Serializer for the Group model
class GroupSerializer(serializers.ModelSerializer):
    # Add related fields if needed for nested representations
    class Meta:
        model = Group
        fields = '__all__'  # Include all fields from the model

# Serializer for the Expense model
class ExpenseSerializer(serializers.ModelSerializer):
    # Add related fields if needed for nested representations
    class Meta:
        model = Expense
        fields = '__all__'

# Serializer for the Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Serializer for the Settlement model
class SettlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement
        fields = '__all__'

# Serializer for the RecurringExpense model
class RecurringExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurringExpense
        fields = '__all__'

# Serializer for the ExpenseTag model
class ExpenseTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseTag
        fields = '__all__'

# Serializer for the SavingsGoal model
class SavingsGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsGoal
        fields = '__all__'
