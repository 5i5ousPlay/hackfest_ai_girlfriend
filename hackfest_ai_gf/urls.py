"""
URL configuration for hackfest_ai_gf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from payment.views import xendit_webhook

urlpatterns = [
    path('admin/', admin.site.urls),

    # CHATBOT
    path('api/v1/', include('chatbot.urls')),

    # USERS & AUTHENTICATION
    path('api/v1/users/', include('users.urls')),

    # PAYMENT
    path('api/v1/payment/', include('payment.urls')),

    # XENDIT WEBHOOK
    path('payment/xendit-webhook/', xendit_webhook, name='xendit-webhook')
]
