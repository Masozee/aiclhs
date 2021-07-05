from django.shortcuts import render
from .models import *


# Create your views here.
def page_not_found_view(request):
     return render(request,'web/404.html')

def Home(request):
    event = Event.objects.all()
    eventdate = Event.objects.all()
    pembicara = Pembicara.objects.all().distinct()[:4]
    listpembicara = ListPembicara.objects.all()
    artikel = Artikel.objects.all().distinct()[:3]

    context = {
        "event": event,
        "eventdate": eventdate,
        "pembicara": pembicara,
        "listpembicara": listpembicara,
        "artikel": artikel,
    }
    return render(request, "web/index.html", context)

def event(request):
    event = Event.objects.all()
    listpembicara = ListPembicara.objects.all()

    context = {
        "event": event,
        "listpembicara": listpembicara,
    }
    return render(request, "web/schedule.html", context)

def Speakers(request):
    pembicara = Pembicara.objects.all()

    context = {

        "pembicara": pembicara,

    }
    return render(request, "web/speakers.html", context)

def Tulisan(request):
    artikel = Artikel.objects.all()

    context = {
        "artikel": artikel,
    }
    return render(request, "web/blog.html", context)

def TulisanDetail(request, artikel_slug):
    artikel = Artikel.objects.get(Slug=artikel_slug)
    

    context = {
        "artikel": artikel,
     
    }
    return render(request, "web/blog-single.html", context)