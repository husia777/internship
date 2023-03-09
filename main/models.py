from django.contrib.auth.models import AbstractUser
from django.db import models
from urllib.parse import urlparse


class SocialLink(models.Model):
    url = models.URLField(max_length=255, default='http://garinv.online:8000/home/')

    def url_text(self):
        parsed_url = urlparse(self.url)
        return parsed_url.hostname.replace("www.", "") + "/..."


class HeroHeaderContent(models.Model):
    content = models.CharField(max_length=255)
    description = models.TextField(default='')
    url = models.URLField(max_length=255, default='http://garinv.online:8000/home/')

    def url_text(self):
        parsed_url = urlparse(self.url)
        return parsed_url.hostname.replace("www.", "") + "/..."


class StatisticContent(models.Model):
    url = models.URLField(max_length=255, default='http://garinv.online:8000/home/')
    content = models.CharField(max_length=255, default='')
    description = models.TextField(default='')

    def url_text(self):
        parsed_url = urlparse(self.url)
        return parsed_url.hostname.replace("www.", "") + "/..."


class Resources(models.Model):
    title = models.CharField(max_length=60)
    url = models.URLField(max_length=255, default='http://garinv.online:8000/home/')

    def url_text(self):
        parsed_url = urlparse(self.url)
        return parsed_url.hostname.replace("www.", "") + "/..."


class Headers(models.Model):
    title = models.CharField(max_length=60)
    url = models.URLField(max_length=255, default='http://garinv.online:8000/home/')


class User(AbstractUser):
    subscribe_to_the_newsletter = models.BooleanField(default=False)
