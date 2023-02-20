from django.urls import path
from django.contrib.auth.views import LogoutView

from config import settings
from main.views import HomePageView, LoginUserView, RegisterUserView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path("logout/", LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),
]

