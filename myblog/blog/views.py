from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.utils import timezone
from .models import Post

class HomeView(TemplateView):
    template_name = "post_list.html"

    def posts(self):
        return Post.objects.all()