from django.urls import path
from .views import ApiIndexView


urlpatterns = [
    path("api/", ApiIndexView.as_view(), name="index"),
]