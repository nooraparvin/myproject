from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name='demo'),

   # path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),
    #path('help/', views.help, name='help'),
    #path('detail/', views.detail, name='detail')
]
