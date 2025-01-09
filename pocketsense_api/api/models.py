from django.db import models
from django.contrib.auth.models import User

# Student Model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=255)
    semester = models.IntegerField()
    default_payment_method = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

# Group Model
class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(Student)

    def __str__(self):
        return self.name

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Expense Model
class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    split_type = models.CharField(max_length=50, choices=[('equal', 'Equal'), ('unequal', 'Unequal')])
    date = models.DateField()
    receipt_image = models.ImageField(upload_to='receipts/', null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.amount} - {self.group.name}"

# Settlement Model
class Settlement(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)
    settlement_method = models.CharField(max_length=50)
    due_date = models.DateField()

    def __str__(self):
        return f"Settlement for {self.expense}"

# RecurringExpense Model
class RecurringExpense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=50, choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')
    ])
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"Recurring {self.amount} ({self.frequency})"

# ExpenseTag Model
class ExpenseTag(models.Model):
    tag_name = models.CharField(max_length=50)
    tag_color = models.CharField(max_length=7, default="#000000")  # Hex color codes
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name='tags')

    def __str__(self):
        return self.tag_name

# SplitHistory Model
class SplitHistory(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    changes_made_by = models.ForeignKey(Student, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    previous_split = models.TextField()
    new_split = models.TextField()

    def __str__(self):
        return f"History for {self.expense} by {self.changes_made_by}"

# SavingsGoal Model
class SavingsGoal(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    saved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()

    def __str__(self):
        return self.goal_name