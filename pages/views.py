from django.shortcuts import render


# Create your views here.


def homepage(request):
    content_html = open('pages/content/index.html').read()
    context = {
        'content': content_html
    }
    return render(request, 'base.html', context)

