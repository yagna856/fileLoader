from django.urls import path
from fileLoad import views

urlpatterns = [
    path("", views.upload, name="upload"),
    path("validate/", views.validate, name="validate"),
]