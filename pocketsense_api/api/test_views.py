from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Student, Group, SavingsGoal


class StudentViewSetTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="alice", password="password")
        self.user2 = User.objects.create_user(username="bob", password="password")
        self.student1 = Student.objects.create(user=self.user1, college="ABC College", semester=1,
                                               default_payment_method="Card")
        self.student2 = Student.objects.create(user=self.user2, college="XYZ College", semester=2,
                                               default_payment_method="Cash")

        self.token = Token.objects.create(user=self.user1)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_filter_by_college(self):
        url = reverse('student-filter-by-college')
        response = self.client.get(url, {'college': 'ABC College'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check response structure
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['user']['username'], "alice")


class GroupViewSetTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="alice", password="password")
        self.user2 = User.objects.create_user(username="bob", password="password")
        self.student1 = Student.objects.create(user=self.user1, college="ABC College", semester=1, default_payment_method="Card")
        self.student2 = Student.objects.create(user=self.user2, college="XYZ College", semester=2, default_payment_method="Cash")

        self.group = Group.objects.create(name="Test Group", description="A test group")
        self.group.members.add(self.student1, self.student2)

        self.token = Token.objects.create(user=self.user1)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_group_members(self):
        url = reverse('group-get-group-members', kwargs={'pk': self.group.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)


class SavingsGoalViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.group = Group.objects.create(name="Test Group", description="A test group")
        self.savings_goal = SavingsGoal.objects.create(
            group=self.group,
            goal_name="New Laptop",
            target_amount=1000.00,
            saved_amount=200.00,
            deadline="2025-12-31"
        )

        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_update_savings_goal_progress(self):
        url = reverse('savingsgoal-update-progress', kwargs={'pk': self.savings_goal.id})
        data = {"saved_amount": 100.00}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['message'], "Goal New Laptop updated successfully!")

        self.savings_goal.refresh_from_db()
        self.assertEqual(self.savings_goal.saved_amount, 300.00)
