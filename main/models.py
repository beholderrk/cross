from django.db import models
from datetime import datetime, date, time


class StatManager(models.Manager):
    def today(self):
        today_min = datetime.combine(date.today(), time.min)
        today_max = datetime.combine(date.today(), time.max)
        return self.filter(created__range=(today_min, today_max))


class Stat(models.Model):
    leader = models.IntegerField(default=0)
    goodsense = models.IntegerField(default=0)
    freeart = models.IntegerField(default=0)
    trust = models.IntegerField(default=0)
    session = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)
    objects = StatManager()