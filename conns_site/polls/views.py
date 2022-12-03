from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse
from .models import Resource


def index(request):
	return TemplateResponse(request, 'index.html')


def resources(request):
	context_data = {'header': ['Автор', 'Проект', 'Ссылка'], 'rows': []}

	resourcesObjs = Resource.objects.all()
	for obj in resourcesObjs:
		context_data['rows'].append(obj)

	return TemplateResponse(request, 'resources.html', context=context_data)
