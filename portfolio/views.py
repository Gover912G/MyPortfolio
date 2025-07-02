from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
  return render(request, 'index.html', {})


def about(request):
  return render(request, 'about.html', {})


def contact(request):
  return render(request, 'contact.html', {})


def portfolio(request):
  project = Project.objects.all()

  context = {
    "projects":project,
  }
  return render(request, 'portfolio.html', context)


def service(request):
  return render(request, 'services.html', {})