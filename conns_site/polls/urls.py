from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('resources/', views.resources, name='resources'),
	path('articles/<int:page>', views.articles, name='articles'),
	path('article/<article_id>/', views.article, name='article'),
]

urlpatterns += staticfiles_urlpatterns()