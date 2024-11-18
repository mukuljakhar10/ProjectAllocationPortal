from django.urls import path
from .views import UserLoginView, UserRegistrationView, TokenRefreshView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('register/', UserRegistrationView.as_view(), name = 'register'),
    path('token/refresh', TokenRefreshView.as_view(), name = 'token_refresh'),
]
