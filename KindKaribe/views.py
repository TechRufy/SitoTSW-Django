from django.shortcuts import render

# Create your views here.

from django import views


class Home(views.generic.TemplateView):
    template_name = "home.html"
