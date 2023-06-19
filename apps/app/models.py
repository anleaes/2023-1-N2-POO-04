from django.db import models

# Create your models here.

class App(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    
    class Meta:
        verbose_name = 'app'
        verbose_name_plural = 'apps'
        ordering =['id']

    def __str__(self):
        return self.name