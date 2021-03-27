from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExpenseType(models.Model):
    expense_type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.expense_type


class ExpenseDescription(models.Model):
    expense_type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Expense(models.Model):
    class UserExpensesManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter()
            
    exp_type= models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    description = models.ForeignKey(ExpenseDescription, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateField()

    #user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #managers
    objects = models.Manager()
    user_objects = UserExpensesManager()

    def __str__(self):
        return f'Expense of: {self.description}'