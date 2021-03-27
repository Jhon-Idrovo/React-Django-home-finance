from django.urls import path
from .views import BlacklistTokenView

app_name = 'login'

urlpatterns = [
    path('logout/', BlacklistTokenView.as_view(), name='logout'),
]