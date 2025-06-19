from django.db import models
from django.utils import timezone
from datetime import timedelta

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rent_due_date = models.DateField()
    notify_30_days = models.TimeField(null=True, blank=True)
    notify_60_days = models.TimeField(null=True, blank=True)
    notify_90_days = models.TimeField(null=True, blank=True)
    email_sent_30 = models.BooleanField(default=False)
    email_sent_60 = models.BooleanField(default=False)
    email_sent_90 = models.BooleanField(default=False)

    def __str__(self):
        return self.name
