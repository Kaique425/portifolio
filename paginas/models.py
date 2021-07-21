from autoslug import AutoSlugField
from enum import unique
from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class Tecnologias(models.Model):
    tec_nome = models.CharField(max_length=255)


    def __str__(self):
        return self.tec_nome

class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    thumbnailHome = models.ImageField(upload_to='images', blank=True,null=True)
    projlink = models.CharField(max_length=255, blank=True, null=True)
    thumbnailDetail = models.ImageField(upload_to='images', blank=True,null=True)
    slug = slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")
    descricao = models.CharField(max_length=255)
    #-Relação  de muito para muitos
    tec_nome = models.ManyToManyField(Tecnologias)

    def __str__(self):
        return self.nome

