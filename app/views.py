from django.shortcuts import render

from app.models import Image


def home(request):
    context = {"images": Image.objects.all()}
    return render(request, "index.html", context)
