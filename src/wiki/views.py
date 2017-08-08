from django.shortcuts import render
from dilesmo.views import HomePage

# Create your views here.
home_page = HomePage.as_view()
#def home_page():
#    pass