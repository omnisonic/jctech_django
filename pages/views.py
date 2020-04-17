from django.shortcuts import render


# Create your views here.


def homepage(request):
    context = {}
    return render(request, 'index.html', context)

def bio(request):
    content_html = open('pages/content/bio.html').read()
    context = {
        'content': content_html
    }
    return render(request, 'base.html', context)

def blog(request):
    content_html = open('pages/content/blog.html').read()
    context = {
        'content': content_html
    }
    return render(request, 'base.html', context)

def contact(request):
    content_html = open('pages/content/contact.html').read()
    context = {
        'content': content_html
    }
    return render(request, 'base.html', context)

def projects(request):
    content_html = open('pages/content/projects.html').read()
    context = {
        'content': content_html
    }
    return render(request, 'base.html', context)