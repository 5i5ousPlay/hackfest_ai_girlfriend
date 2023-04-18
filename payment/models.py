import uuid

from django.db import models
from users.models import CustomUser
# Create your models here.


class Payment(models.Model):

    # POSSIBLE PAYMENT STATUSES
    PAID = 'PAID'
    PENDING = 'PENDING'
    EXPIRED = 'EXPIRED'
    STATUS_CHOICES = [
        (PAID, 'PAID'),
        (PENDING, 'PENDING'),
        (EXPIRED, 'EXPIRED')
    ]

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(CustomUser, related_name='payment', on_delete=models.CASCADE, null=True)
    xendit_id = models.CharField(max_length=255, null=True, blank=True, default='')
    reference_id = models.CharField(max_length=255, null=True, blank=True, default='')
    amount = models.FloatField(default=2000, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=PENDING)
    expiry_date = models.CharField(max_length=255, null=True, blank=True, default='')
    paid_at = models.CharField(max_length=255, null=True, blank=True, default='PENDING')
    payment_method = models.CharField(max_length=255, null=True, blank=True, default='PENDING')
    created = models.CharField(max_length=255, null=True, blank=True, default='')
    updated = models.CharField(max_length=255, null=True, blank=True, default='')
