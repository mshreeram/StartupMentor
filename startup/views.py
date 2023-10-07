from django.shortcuts import render
from django.http import HttpResponse

def home(req):
  return render(req, 'home.html')

def registerAsMentor(req):
  return render(req, 'mentor/register.html')

def registerAsStartUp(req):
  return render(req, 'startup/register.html')

def registerAsStudent(req):
  return render(req, 'student/register.html')

def loginAsMentor(req):
  return render(req, 'mentor/login.html')

def loginAsStartUp(req):
  return render(req, 'startup/login.html')

def loginAsStudent(req):
  return render(req, 'student/login.html')