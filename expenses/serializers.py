from rest_framework import serializers
from .models import Expense, ExpenseDescription, ExpenseType

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseType


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseDescription

        