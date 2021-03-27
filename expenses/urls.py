from django.urls import path
from django.views.generic import TemplateView
from .views import CreateExpenses

app_name = 'expenses'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('save-expenses/', CreateExpenses.as_view())
]