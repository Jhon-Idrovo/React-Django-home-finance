from django.urls import path
from .views import ExpensesList, CreateUser, ExpenseStats

app_name = 'statistics_API'

urlpatterns = [
    path('all-expenses/', ExpensesList.as_view(), name='list'),
    path('register/', CreateUser.as_view(), name='register'),
    path('statistics/', ExpenseStats.as_view(), name='stats'),
]