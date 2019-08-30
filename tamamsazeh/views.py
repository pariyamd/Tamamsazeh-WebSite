from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def projects(request):
    return render(request=request,template_name='projects.html')
def main_page(request):
    return render(request=request,template_name='main_page.html')
def base(request):
    return render(request=request,template_name='base.html')
def certifications(request):
    return render(request=request,template_name='certifications.html')
def aboutus(request):
    return render(request=request,template_name='aboutus.html')