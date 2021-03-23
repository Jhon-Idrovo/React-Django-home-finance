from rest_framework import serializers
from expenses.models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    exp_type = serializers.StringRelatedField()
    description = serializers.StringRelatedField()
    
    class Meta:
        model = Expense
        exclude = ['user']