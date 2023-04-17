from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.core.exceptions import ValidationError as DjangoValidationError


class CustomRegisterSerializer(RegisterSerializer):
    mobile_number = PhoneNumberField(region='PH')
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    number_of_dependents = serializers.IntegerField(required=True)
    monthly_income = serializers.FloatField(required=True)
    medical_conditions = serializers.CharField(required=True)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'mobile_number': self.validated_data.get('mobile_number', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'age': self.validated_data.get('age', ''),
            'number_of_dependents': self.validated_data.get('number_of_dependents', ''),
            'monthly_income': self.validated_data.get('monthly_income', ''),
            'medical_conditions': self.validated_data.get('medical_conditions', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data['password1'], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
            )
        user.mobile_number = self.cleaned_data['mobile_number']
        user.age = self.cleaned_data['age']
        user.number_of_dependents = self.cleaned_data['number_of_dependents']
        user.monthly_income = self.cleaned_data['monthly_income']
        user.medical_conditions = self.cleaned_data['medical_conditions']
        user.save()
        self.custom_signup(request, user)
        setup_user_email(request, user, [])

        return user
