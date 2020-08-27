from datetime import date
from django.db import models
from django.contrib.auth import get_user_model

from projects.models import Project

User = get_user_model()


class Naver(models.Model):
    name = models.CharField('Nome', max_length=55, blank=False)
    birthdate = models.DateField('Data de Nascimento', default=date.today, blank=False)
    admission_date = models.DateField('Data de Admissão', default=date.today, blank=False)
    job_role = models.CharField('Cargo de Trabalho', max_length=255, blank=False)

    projects = models.ManyToManyField(
        Project, verbose_name='Projeto',
        related_name='navers',
    )
    user = models.ForeignKey(
        User, verbose_name='Usuário',
        related_name='navers',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Naver'
        verbose_name_plural = 'Navers'
        ordering = ['name']
