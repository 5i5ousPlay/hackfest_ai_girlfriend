from django.urls import path, include
from .views import PaymentCreateView, PaymentListView, create_checkout_session

urlpatterns = [
    path('paymentcreate/', PaymentCreateView.as_view()),
    path('paymentlist/', PaymentListView.as_view()),
    path('create-checkout-session/<str:id>/', create_checkout_session, name='create-checkout-session'),
]