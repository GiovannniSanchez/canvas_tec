from django.shortcuts import render
import openai


def index(request):
    return render(request, 'Mfeni/index.html')
