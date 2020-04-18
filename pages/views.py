import requests
from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class BlogPageView(TemplateView):
    template_name = 'blog.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

def projects(request):
    response = requests.get('https://api.github.com/users/omnisonic/repos')
    repos = response.json()
    repo_list = repos[0]['html_url']
    results = []
    for item in repos:
        results.append(item['html_url'])
    print('hello\n' + '\n'.join(results))
    str1 = '\n '.join(results)

        
    context = {
        'github_repos': str1,
    }
    return render(request, 'projects.html', context)


def getGithubLinks(request):
    response = requests.get('https://api.github.com/users/omnisonic/repos')
    repos = response.json()
    repo_list = repos[0]['html_url']
    for i in repos:
        repo_list += [i]
        return repo_list

