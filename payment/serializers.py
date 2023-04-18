from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    amount = serializers.FloatField(default=2000)
    class Meta:
        model = Payment
        fields = ['id', 'xendit_id', 'reference_id', 'amount', 'description',
                  'user', 'status', 'paid_at', 'payment_method', 'expiry_date',
                  'created', 'updated']
        read_only_fields = ['user', 'description', 'status', 'xendit_id',
                            'reference_id', 'payment_method', 'expiry_date', 'paid_at',
                            'created', 'updated']
        extra_kwargs = {
            'amount': {'min_value': 0, 'max_value': None}
        }