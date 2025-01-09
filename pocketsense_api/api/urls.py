from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    StudentViewSet, GroupViewSet, ExpenseViewSet, CategoryViewSet, SettlementViewSet,
    home, RecurringExpenseViewSet, SavingsGoalViewSet
)

# Create the router for viewsets
router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'expenses', ExpenseViewSet, basename='expense')  # Use a single registration with a basename
router.register(r'categories', CategoryViewSet)
router.register(r'settlements', SettlementViewSet)
router.register(r'recurring-expenses', RecurringExpenseViewSet)
router.register(r'savings-goals', SavingsGoalViewSet)

# Combine router URLs with custom action URLs
urlpatterns = [
    # path('', home, name='home'),  # Root path for the home view
    path('', include(router.urls)),  # Include all router-generated URLs
]

# Add custom action URLs explicitly to the router-generated urlpatterns
urlpatterns += [
    path('students/by-college/', StudentViewSet.as_view({'get': 'filter_by_college'}), name='student-filter-by-college'),
    path('groups/<int:pk>/members/', GroupViewSet.as_view({'get': 'get_group_members'}), name='group-get-group-members'),
    path('savings-goals/<int:pk>/update-progress/', SavingsGoalViewSet.as_view({'post': 'update_progress'}), name='savingsgoal-update-progress'),
]
