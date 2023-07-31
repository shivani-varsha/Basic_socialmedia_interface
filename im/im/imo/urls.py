from django.urls import path
from . import views

urlpatterns = [
    path('upload',views.upload,name='upload'),
    path('main',views.main,name='main')

]