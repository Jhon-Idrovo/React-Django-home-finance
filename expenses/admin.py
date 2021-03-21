from django.contrib import admin
from .models import Expense, ExpenseDescription, ExpenseType
# Register your models here.

admin.site.register(Expense)
admin.site.register(ExpenseType)
admin.site.register(ExpenseDescription)