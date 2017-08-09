from django.shortcuts import render
#from dilesmo.views import HomePage

# Create your views here.
#def home_page(request):
 #   return HomePage.as_view()

def query_page(request):
    return render(request, 'wiki/query.html')


def results_page(request):
    return render(request, 'wiki/results.html')