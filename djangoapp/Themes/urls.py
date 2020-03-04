from django.urls import path
from . import views
urlpatterns = [
path('', views.theme_view, name= "theme_view")
]