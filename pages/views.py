from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

def homepage(request):
    context = {}
    return render(request, 'home.html', context)