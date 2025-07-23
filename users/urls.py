from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, UserOrderHistoryView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('orders/', UserOrderHistoryView.as_view(), name='order-history'),
]