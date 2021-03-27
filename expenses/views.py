import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import get_user
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import ExpenseSerializer, DescriptionSerializer, TypeSerializer
from .models import Expense,ExpenseDescription, ExpenseType

class CreateExpenses(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        user = request.user
        print(22, user)
        for expense in request.data:
            print(expense)
            exp_type, created =ExpenseType.objects.get_or_create(expense_type=expense['expType'], user=user)
            description,created = ExpenseDescription.objects.get_or_create(expense_type=exp_type,description=expense['description'],user=user)
            expense = Expense.objects.create(user= user, exp_type=exp_type, description= description, amount = expense['amount'], date=datetime.date.today())
            print(expense)
        return Response(status=status.HTTP_201_CREATED)