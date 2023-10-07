from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.home, name="home"),
  path('registerAsMentor/', views.registerAsMentor, name="registerAsMentor"),
  path('registerAsStartUp/', views.registerAsStartUp, name="registerAsStartUp"),
  path('registerAsStudent/', views.registerAsStudent, name="registerAsStudent"),
  path('Mentors/', views.Mentors, name="Mentors"),
  path('StartUps/', views.StartUps, name="StartUps"),
  path('Students/', views.Students, name="Students"),
]