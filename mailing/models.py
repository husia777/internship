from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from config.settings import EMAIL_HOST_USER
from main.models import User
# signals imports
from django.dispatch import receiver
from django.db.models.signals import post_save


class MailSubscribedToTheNewsletter(models.Model):
    email = models.EmailField()


class Mailing(models.Model):
    description = models.TextField(default='')
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Mailing)
def mail_send_for_subscribers(sender, instance, created, *args, **kwargs):
    if created:
        users = User.objects.filter(subscribe_to_the_newsletter=True)
        emails = MailSubscribedToTheNewsletter.objects.all()

        context = {
            "title": instance.title,
            "content": instance.description
        }
        html_content = render_to_string('html/main.html', context)
        text_content = strip_tags(html_content)
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
