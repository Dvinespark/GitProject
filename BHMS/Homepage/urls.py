from django.conf.urls import url
from .import views


urlpatterns =[

    url(r'^$',views.Index, name='index'),
    url(r'^$',views.user_register, name='register'),


]