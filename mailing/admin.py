from django.contrib import admin
from .models import Mailing, MailSubscribedToTheNewsletter


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    pass


@admin.register(MailSubscribedToTheNewsletter)
class MailSubscribedToTheNewsletterAdmin(admin.ModelAdmin):
    pass
