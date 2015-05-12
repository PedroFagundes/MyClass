from django.db import models


class Materias(models.Model):
	nome = models.CharField(max_length=45)

	def __str__(self):
		return self.nome