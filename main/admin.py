from django.contrib import admin
from main.models import Stat


class StatAdmin(admin.ModelAdmin):
    list_display = ('leader', 'goodsense', 'freeart', 'trust', 'session', 'created', 'modify')


admin.site.register(Stat, StatAdmin)