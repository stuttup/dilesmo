from django.shortcuts import render
from django.http import HttpResponse
#from dilesmo.views import HomePage

# Create your views here.
#def home_page(request):
 #   return HomePage.as_view()

def query_page(request):
    return render(request, 'wiki/query.html', {
        'new_image': request.POST.get("query", ''),
    })


def results_page(request):
    return render(request, 'wiki/results.html')