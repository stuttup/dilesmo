from django.shortcuts import render
from dilesmo.views import HomePage

# Create your views here.
def home_page(request):
    return HomePage.as_view()