from django.urls import path
from django.contrib.auth.views import LogoutView

from config import settings
from main.views import home, LoginUserView, RegisterUserView, subscribe_to_the_newsletter

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path("logout/", LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),
    path('email_current/', subscribe_to_the_newsletter, name='email_current')

]

