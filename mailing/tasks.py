import os
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from config.settings import EMAIL_HOST_USER
from main.models import User
# signals imports

from celery import shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


@shared_task
def mail_task( context, html_content, text_content,*users, emails, **kwargs):

    context = context
    html_content = html_content
    text_content = text_content
    for user in users:
        email = EmailMultiAlternatives(
            "Test HTML Email",
            text_content,
            EMAIL_HOST_USER,
            [user.email]
        )
        email.attach_alternative(html_content, 'text/html')
        email.send()

    for email in emails:
        email = EmailMultiAlternatives(
            "Test HTML Email",
            text_content,
            EMAIL_HOST_USER,
            [email.email]
        )
        email.attach_alternative(html_content, 'text/html')
        email.send()
    return


