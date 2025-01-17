# Generated by Django 4.2.17 on 2025-01-06 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('split_type', models.CharField(choices=[('equal', 'Equal'), ('unequal', 'Unequal')], max_length=50)),
                ('date', models.DateField()),
                ('receipt_image', models.ImageField(blank=True, null=True, upload_to='receipts/')),
                ('anonymous', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=255)),
                ('semester', models.IntegerField()),
                ('default_payment_method', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SplitHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('previous_split', models.TextField()),
                ('new_split', models.TextField()),
                ('changes_made_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student')),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.expense')),
            ],
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.BooleanField(default=False)),
                ('settlement_method', models.CharField(max_length=50)),
                ('due_date', models.DateField()),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.expense')),
            ],
        ),
        migrations.CreateModel(
            name='SavingsGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=100)),
                ('target_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saved_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('deadline', models.DateField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.group')),
            ],
        ),
        migrations.CreateModel(
            name='RecurringExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('frequency', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('yearly', 'Yearly')], max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(to='api.student'),
        ),
        migrations.CreateModel(
            name='ExpenseTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
                ('tag_color', models.CharField(default='#000000', max_length=7)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='api.expense')),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.group'),
        ),
    ]
