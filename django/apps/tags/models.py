from django.db import models

from django.core.urlresolvers import reverse
from django.db import models

# Nodes - nodes of learning graph

class SubjectTag(models.Model):
    title = models.CharField('Название объекта', max_length=300)

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'

    def __str__(self):
        return self.title