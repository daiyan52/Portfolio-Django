from django.shortcuts import render
from django.views.generic import TemplateView

class  homeView(TemplateView):
    template_name = "pages/home.html"
    

class citybeatView(TemplateView):
    template_name = "pages/citybeat.html"

class quizAppView(TemplateView):
    template_name = "pages/quizApp.html"

class footFusionView(TemplateView):
    template_name = "pages/footFusion.html"