from django.contrib import admin
from main.models import Stat


class StatAdmin(admin.ModelAdmin):
    list_display = ('leader', 'goodsense', 'freeart', 'trust', 'session', 'created', 'modify')
    list_filter = ('leader', 'goodsense', 'freeart', 'trust', 'created', 'modify')
    date_hierarchy = 'created'


admin.site.register(Stat, StatAdmin)