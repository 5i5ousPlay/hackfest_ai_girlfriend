from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Create your views here.
tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-large')
model = AutoModelForCausalLM.from_pretrained('microsoft/DialoGPT-large')
# bot = pipeline('text-generation', model=model, tokenizer=tokenizer)
bot = pipeline(model='gpt2', max_new_tokens=100)
@csrf_exempt
@api_view(['POST'])
def chat(request):
    user_message = request.data['message']
    print(request.data)
    print(bot)
    # bot_response = bot(user_message)[0]['generated_text']
    response = bot(user_message)[0]['generated_text']
    return JsonResponse({'bot_response': response})
    # return render(bot_response, 'app/chat.html' )