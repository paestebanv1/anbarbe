from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from .serializer import NewSerializer
from .models import News

# Create your views here.

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewSerializer

def news(request):
    news = list(News.objects.all())
    return JsonResponse(news, safe=False)

def new(request, newid):
    return HttpResponse("Esta es la vista de una noticia con el ID " + newid)

def unews(request):
    return HttpResponse(" Esta es la vista de noticias Urgentes ")

def nunews(request):
    return HttpResponse(" esta es la vista de noticias No Urgentes ")

def pnews(request):
    return HttpResponse(" Esta es la vista de noticias periodicas ")

