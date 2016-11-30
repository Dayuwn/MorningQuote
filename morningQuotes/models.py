from django.db import models

# Create your models here.
class MorningQuote(models.Model):
	quote = models.CharField(max_length=2048)
	author = models.CharField(max_length=255)
	imageURL = models.URLField()
	date = models.DateField(auto_now_add=True)