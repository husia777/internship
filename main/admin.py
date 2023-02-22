from django.contrib import admin

from main.models import Headers


@admin.register(Headers)
class HeadersAdmin(admin.ModelAdmin):
    pass
