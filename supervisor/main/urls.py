from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('allocation/', views.generated, name='list'),
    path('file/<str:file_name>', views.download, name='file_res'),

]