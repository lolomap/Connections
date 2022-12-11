from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('resources/', views.resources, name='resources'),
	path('article/<article_id>/', views.article, name='article'),
	path('<article_id>/', views.article, name='article')
]

urlpatterns += staticfiles_urlpatterns()