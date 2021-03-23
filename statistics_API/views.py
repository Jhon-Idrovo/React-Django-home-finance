from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAuthenticated

from .serializers import ExpenseSerializer, StatsSerializer
from expenses.models import Expense 
# Create your views here.

class PostUserWriteExpense(BasePermission):
    message = 'No tiene acceso a este contenido'

    def has_object_permission(self, request, view, obj):
        print(request)
        return request.user == obj.user


class ExpensesList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user=self.request.user
        return user.expense_set.all()

class ExpenseStats(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StatsSerializer
    
