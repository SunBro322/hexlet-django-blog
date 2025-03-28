from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def index(request, tags, article_id):
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")

