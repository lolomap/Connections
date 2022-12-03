from django.db import models

# Create your models here.
class Resource(models.Model):
	author = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	link = models.URLField()

class Article(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	author = models.CharField(max_length=100)
	source = models.URLField()