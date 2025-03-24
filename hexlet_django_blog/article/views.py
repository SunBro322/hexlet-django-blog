from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('article')
        return render(request, 'articles.html', context={
        'name': 'Articles',
    })
