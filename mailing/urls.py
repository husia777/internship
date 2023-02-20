from django.urls import path
from mailing.views import email_subscription

urlpatterns = [
    path('email/', email_subscription, name='email'),
]
