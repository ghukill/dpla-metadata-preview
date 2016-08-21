from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template

# Create your views here.

def index(request):
	context = {}
	return render(request, 'dplamp/index.html', context)
