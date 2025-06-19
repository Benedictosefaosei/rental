from celery import shared_task
from datetime import date, timedelta, datetime
from django.core.mail import send_mail
from .models import Tenant

@shared_task
def send_rent_reminders():
    today = date.today()

    for tenant in Tenant.objects.all():
        days_to_due = (tenant.rent_due_date - today).days
        now = datetime.now().time()

        if days_to_due == 90 and not tenant.email_sent_90:
            if not tenant.notify_90_days or now >= tenant.notify_90_days:
                send_mail(
                    subject="90 Days Rent Reminder",
                    message=f"Dear {tenant.name}, your rent is due in 90 days.",
                    from_email=None,
                    recipient_list=[tenant.email],
                )
                tenant.email_sent_90 = True

        if days_to_due == 60 and not tenant.email_sent_60:
            if not tenant.notify_60_days or now >= tenant.notify_60_days:
                send_mail(
                    subject="60 Days Rent Reminder",
                    message=f"Dear {tenant.name}, your rent is due in 60 days.",
                    from_email=None,
                    recipient_list=[tenant.email],
                )
                tenant.email_sent_60 = True

        if days_to_due == 30 and not tenant.email_sent_30:
            if not tenant.notify_30_days or now >= tenant.notify_30_days:
                send_mail(
                    subject="30 Days Rent Reminder",
                    message=f"Dear {tenant.name}, your rent is due in 30 days.",
                    from_email=None,
                    recipient_list=[tenant.email],
                )
                tenant.email_sent_30 = True

        tenant.save()
