from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.home, name="home"),
  path('registerAsMentor/', views.registerAsMentor, name="registerAsMentor"),
  path('registerAsStartUp/', views.registerAsStartUp, name="registerAsStartUp"),
  path('registerAsStudent/', views.registerAsStudent, name="registerAsStudent"),
  path('loginAsMentor/', views.loginAsMentor, name="loginAsMentor"),
  path('loginAsStartUp/', views.loginAsStartUp, name="loginAsStartUp"),
  path('loginAsStudent/', views.loginAsStudent, name="loginAsStudent"),
]