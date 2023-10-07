from django.shortcuts import render
from .models import Mentor, StartUp, Student

def home(req):
  return render(req, 'home.html')

def registerAsMentor(req):
  if req.method == "POST":
    mentor = Mentor()
    mentor.name = req.POST['name']
    mentor.description = req.POST['description']
    mentor.domains = req.POST['domains']
    mentor.email = req.POST['email']

    mentor.save()

  return render(req, 'mentor/register.html')

def registerAsStartUp(req):
  if req.method == "POST":
    startup = StartUp()
    startup.name = req.POST['name']
    startup.description = req.POST['description']
    startup.domains = req.POST['domains']
    startup.email = req.POST['email']

    startup.save()

  return render(req, 'startup/register.html')

def registerAsStudent(req):
  if req.method == "POST":
    student = Student()
    student.name = req.POST['name']
    student.description = req.POST['description']
    student.domains = req.POST['domains']
    student.email = req.POST['email']

    student.save()

  return render(req, 'student/register.html')

def Mentors(req):
  mentors = Mentor.objects.all()
  return render(req, 'mentor/Mentors.html', { 'mentors': mentors })

def StartUps(req):
  startups = StartUp.objects.all()
  return render(req, 'startup/StartUps.html', { 'startups': startups })

def Students(req):
  students = Student.objects.all()
  return render(req, 'student/Students.html', { 'students': students })