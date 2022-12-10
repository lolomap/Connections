from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse
from .models import Resource, Article


def index(request):
	return TemplateResponse(request, 'index.html')


def resources(request):
	context_data = {'header': ['Автор', 'Проект', 'Ссылка'], 'rows': []}

	resourcesObjs = Resource.objects.all()
	for obj in resourcesObjs:
		context_data['rows'].append(obj)

	return TemplateResponse(request, 'resources.html', context=context_data)

def article(request, article_id):
	aid = article_id.replace('-', ' ')
	try:
		articleObj = Article.objects.get(title=aid)
		context_data = {'article': articleObj}
		return TemplateResponse(request, 'article.html', context=context_data)
	except ObjectDoesNotExist:
		return HttpResponse(f'Статья {aid} не существует')