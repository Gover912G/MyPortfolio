
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name = 'home'),
  path('about', views.about, name = 'about'),
  path('contact', views.contact, name = 'contact'),
  path('portfolio', views.portfolio, name = 'portfolio'),
  path('service', views.service, name = 'services'),
 # path('', views.home, name = 'home'),
 # path('', views.home, name = 'home'),

   
]
