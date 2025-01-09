from django.test import TestCase
from .models import SavingsGoal, Group


class SavingsGoalModelTests(TestCase):
    def test_savings_goal_creation(self):
        # Manually create a Group object
        group = Group.objects.create(name="Test Group")

        # Create a SavingsGoal object using the ORM
        savings_goal = SavingsGoal.objects.create(
            group=group,
            goal_name="Vacation Fund",
            target_amount=1000,
            saved_amount=100,
            deadline="2025-12-31"
        )

        # Assert the values of the SavingsGoal instance
        self.assertEqual(savings_goal.goal_name, "Vacation Fund")
        self.assertEqual(savings_goal.target_amount, 1000)
        self.assertEqual(savings_goal.saved_amount, 100)
        self.assertEqual(str(savings_goal.deadline), "2025-12-31")
