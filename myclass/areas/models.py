from django.db import models

# Create your models here.
class Areas(models.Model):
	nome = models.CharField(max_length=45)

	def __str__(self):
		return self.nome