from django.contrib import admin
from .models import Tenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rent_due_date')


# from django_celery_beat.models import PeriodicTask, IntervalSchedule
# admin.site.register(PeriodicTask)
# admin.site.register(IntervalSchedule)
