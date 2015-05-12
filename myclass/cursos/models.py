from django.db import models

from areas.models import Areas
from campus.models import Campus


class Cursos(models.Model):
	nome = models.CharField(max_length=45)
	campus = models.ForeignKey(Campus)
	area = models.ForeignKey(Areas)


	def __str__(self):
		return self.nome