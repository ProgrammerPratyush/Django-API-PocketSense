from rest_framework.test import APITestCase
from rest_framework import status
from .serializers import SavingsGoalSerializer
from .models import SavingsGoal, Group


class SavingsGoalSerializerTests(APITestCase):
    def test_savings_goal_serializer(self):
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

        # Serialize the SavingsGoal object
        serializer = SavingsGoalSerializer(savings_goal)

        # Test if the serialized data matches the model data
        self.assertEqual(serializer.data['goal_name'], savings_goal.goal_name)
        # Use float conversion to handle the decimals
        self.assertEqual(float(serializer.data['target_amount']), float(savings_goal.target_amount))
        self.assertEqual(float(serializer.data['saved_amount']), float(savings_goal.saved_amount))
        self.assertEqual(str(serializer.data['deadline']), "2025-12-31")
