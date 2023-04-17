from django.urls import path, include

urlpatterns = [

    # AUTHENTICATION
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),

]