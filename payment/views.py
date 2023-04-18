import json

from django.shortcuts import render
from .models import Payment
from users.models import CustomUser
from .serializers import PaymentSerializer

from django.conf import settings
from django.http import JsonResponse

from rest_framework import status, generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response

from xendit import Xendit

# Create your views here.


# BYPASS SESSION AUTHENTICATION FORCED CSRF CHECKS
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)


class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    # authentication_classes = [CsrfExemptSessionAuthentication] # FOR DEMO PURPOSES ONLY
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# XENDIT AUTH
api_key = settings.XENDIT_HACKFEST
xendit_instance = Xendit(api_key=api_key)
Invoice = xendit_instance.Invoice


@api_view(['POST'])
@authentication_classes([CsrfExemptSessionAuthentication])
def create_checkout_session(request, id):
    try:
        payment = Payment.objects.get(id=id)
        user = CustomUser.objects.get(id=payment.user.id)
        items = []
        item = {
            'name': str(payment.id),
            'price': payment.amount,
            'quantity': 1,
        }
        items.append(item)

        checkout_session = Invoice.create(
            external_id=f"invoice-{payment.id}",
            amount=payment.amount,
            description=f"Payment for registration fee with reference: invoice-{payment.id}",
            invoice_duration=86400,
            customer={
                'given_names': user.first_name,
                'surname': user.last_name,
                'email': user.email,
                'mobile_number': str(user.mobile_number),
                'address': 'FinMommy'
            },
            items=items,
            payer_email=user.email
        )

        payment.xendit_id = str(checkout_session.id)
        payment.reference_id = str(checkout_session.external_id)
        payment.description = str(checkout_session.description)
        payment.expiry_date = str(checkout_session.expiry_date)
        payment.created = str(checkout_session.created)
        payment.updated = str(checkout_session.updated)
        payment.save()

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JsonResponse({'invoice': checkout_session.invoice_url})


@api_view(['POST'])
@authentication_classes([CsrfExemptSessionAuthentication])
def xendit_webhook(request):
    callback = settings.XENDIT_CALLBACK
    payload = json.loads(request.body)

    if request.META['HTTP_X_CALLBACK_TOKEN'] == callback:
        payment = Payment.objects.get(id=payload['external_id'][8:])
        payment.updated = payload['updated']
        payment.save()

        if payload['status'] == 'PAID':
            payment.status = 'PAID'
            payment.paid_at = payload['paid_at']
            payment.payment_method = payload['payment_method']
            payment.save()

            payment.user.permission_class = 'SUBSCRIBED'
            payment.user.save()

        elif payload['status'] == 'EXPIRED':
            payment.status = payment.paid_at = payment.payment_method = 'EXPIRED'
            payment.save()

    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

    return Response(status=status.HTTP_200_OK)
