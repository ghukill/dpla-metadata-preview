from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template

# import models
from .models import Server, Record


# fire Server instance
server = Server()


# Create your views here.

def index(request):
	context = {}
	return render(request, 'oai/index.html', context)


def xml(request, identifier):
	record = server.get_record(identifier)
	return HttpResponse(record.sickle_api.raw, content_type="application/xml")

def json(request, identifier):
	pass