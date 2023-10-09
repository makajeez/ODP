from django.shortcuts import render
from django.views.generic.list import ListView
from core.helpers import Egg
from .models import GalleryImage



# Create your views here.

class Gallery(ListView):
    template_name = "core/gallery.html"
    model = GalleryImage
    context_object_name = "images"