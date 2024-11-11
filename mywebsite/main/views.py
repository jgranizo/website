# main/views.py
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')  # Make sure this name matches your file
