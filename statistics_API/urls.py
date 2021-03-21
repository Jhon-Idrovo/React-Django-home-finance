from django.urls import path
from .views import ExpensesList

app_name = 'statistics_API'

urlpatterns = [
    path('api/', ExpensesList.as_view(), name='list')
]