from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from users.permissions import IsSubscribed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
import openai

# Create your views here.
openai.api_key = settings.HACKFEST_OPENAI_SECRET_KEY

@csrf_exempt
@api_view(['POST'])
def chat(request):
    user_message = request.data['message']
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a playful financial advisor and also my significant other"},
            {"role": "user", "content": f"{user_message}"}
        ]
    )

    response = completion.choices[0].message

    return JsonResponse({"bot_response": response})

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated & IsSubscribed])
def storyline_view(request):
    # Cheska's Storyline stuff
    pass