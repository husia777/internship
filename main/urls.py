from django.urls import path

from main.views import HomePageView, LoginUserView, RegisterUserView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register')
]

