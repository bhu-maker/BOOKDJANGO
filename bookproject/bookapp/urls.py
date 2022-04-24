from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [path('',views.creating),
              path('list',views.listing),
              path('read/<int:pk>',views.reading),
              path('up/<int:pk>',views.updating),
              path('del/<int:pk>',views.deleting),
              path('api/gett',views.gettingall),
              path('api/postt',views.postting),
              path('api/gett/<str:pk>',views.readgetting)]
