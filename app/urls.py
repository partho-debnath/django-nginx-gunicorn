from django.urls import path

from .views import home, ImageListAPIView

urlpatterns = [
    path(
        "",
        home,
        name="home",
    ),
    path(
        "images/",
        ImageListAPIView.as_view(),
        name="images",
    ),
]
