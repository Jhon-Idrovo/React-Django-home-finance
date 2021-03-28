import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models import Sum

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ExpenseSerializer, StatsSerializer, RegisterUserSerializer
from expenses.models import Expense 
# Create your views here.


class ExpensesList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user=self.request.user
        return user.expense_set.all()

class ExpenseStats(APIView):
    def post(self, request):
        user = request.user
        types = user.expensetype_set.all()
        initial_date = datetime.date.fromisoformat(request.data['init'])
        ending_date = datetime.date.fromisoformat(request.data['end'])

        #First calculate the labels which then can be used to make the queries
        i = initial_date
        labels=[]
        while i<=ending_date:
            month = i.month
            year = i.year
            labels.append(str(year)+'-'+ str(month))
            
            if month==12:
                i=i.replace(year=year+1,month=1)
            else:
                i=i.replace(month=month+1)
                

        #Query the expenses
        series = []
        for exp_type in types:
            values={'label':exp_type.expense_type, 'data':[]}

            for d in labels:
                #calculate the sum of all expenses in the i month
                d=d.split('-')
                year = int(d[0])
                month = int(d[1])
                sum = user.expense_set.filter(
                    exp_type=exp_type,
                    date__month = month,
                    date__year = year
                ).aggregate(Sum('amount'))

                if sum['amount__sum']==None:
                    sum['amount__sum']=0
                print(sum)
                #add the sum to the serie
                values['data'].append(sum['amount__sum'])
                
        data = {'series':series,'labels':labels}
        
        return Response(data,status=status.HTTP_200_OK)

    
