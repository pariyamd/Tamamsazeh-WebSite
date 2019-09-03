from django.shortcuts import render
from django.http import HttpResponse
from tamamsazeh.models import Article,Post

# Create your views here.
def projects(request):
    return render(request=request, template_name='projects.html')


def main_page(request):
    return render(request=request, template_name='main_page.html')


def base(request):
    return render(request=request, template_name='base.html')


def certifications(request, num):
    return render(request=request, template_name='certifications.html', context={"id": num})


def certificationsNon(request):
    return render(request=request, template_name='certifications.html', context={"id": 1})


def aboutus(request):
    return render(request=request, template_name='aboutus.html')


def crew(request):
    return render(request=request, template_name='crew.html')


def article(request):
    return render(request=request, template_name='article.html',context={
       'articles': Article.objects.all()
    })


def articleView(request,link):
    return render(request=request, template_name='articleView.html',context={'link' : link})


def blog(request):
    return render(request=request, template_name='blog.html',context={
        'posts': Post.objects.all()
    })

