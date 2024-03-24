from django.shortcuts import render
from rest_framework.generics import ListAPIView

from app.models import Image
from .serializer import ImageSerializer


def home(request):
    context = {"images": Image.objects.all()}
    return render(request, "index.html", context)


class ImageListAPIView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
