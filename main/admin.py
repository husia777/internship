from django.contrib import admin

from main.models import Headers, SocialLink, Resources, HeroHeaderContent, StatisticContent


@admin.register(Headers)
class HeadersAdmin(admin.ModelAdmin):
    pass


@admin.register(StatisticContent)
class SocialLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(Resources)
class ResourcesAdmin(admin.ModelAdmin):
    pass


@admin.register(HeroHeaderContent)
class HeroHeaderContentAdmin(admin.ModelAdmin):
    pass
