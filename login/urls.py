from django.urls import path
from .views import BlacklistTokenView, CreateUser

app_name = 'login'

urlpatterns = [
    path('logout/', BlacklistTokenView.as_view(), name='logout'),
    path('register/', CreateUser.as_view(), name='register'),
]