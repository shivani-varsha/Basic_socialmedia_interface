from django.urls import path
from . import views
app_name = 'newo'
urlpatterns=[
    path('',views.coder),
    path('sign',views.sign,name="sign"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('settings',views.settings,name='settings')
    ]