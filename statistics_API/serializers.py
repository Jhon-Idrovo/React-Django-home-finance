from rest_framework import serializers
from expenses.models import Expense
from django.contrib.auth.models import User

class ExpenseSerializer(serializers.ModelSerializer):
    exp_type = serializers.StringRelatedField()
    description = serializers.StringRelatedField()
    
    class Meta:
        model = Expense
        exclude = ['user']


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password':{'write_only':True}}

    #we can edit the create method to change the validation process