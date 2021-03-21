from django.shortcuts import render
from rest_framework import generics

from .serializers import ExpenseSerializer
from expenses.models import Expense 
# Create your views here.

class ExpensesList(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer