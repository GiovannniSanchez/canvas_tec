
from django.shortcuts import render
from django.http import HttpResponse

def cuestionario(request):
    return render(request, 'cuestionario.html')
