from django.contrib import admin
from .models import answers_user, AnswersChatgpt

# Register your models here.
admin.site.register(answers_user)
admin.site.register(AnswersChatgpt)