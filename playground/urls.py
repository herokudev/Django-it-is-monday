from django.urls import path
from . import views

#URLConf
urlpatterns = [
  path('', views.index),
  path("<str:name>", views.greet, name="greet"),
  path('brian/', views.brian),
  path('hello/', views.say_hello),
]
