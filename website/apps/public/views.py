from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
