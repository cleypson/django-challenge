import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return "{}".format(self.username)


class Never(models.Model):
    name = models.CharField('Name', max_length=254)
    birthdate = models.DateField('Birthdate')
    admission_date = models.DateField('Admission date')
    job_role = models.CharField('Job role', max_length=128)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em')

    def __str__(self):
        return "#{}-{}".format(self.id, self.name)

    class Meta:
        verbose_name = 'Never'
        verbose_name_plural = 'Nevers'


class Projeto(models.Model):
    name = models.CharField('Name', max_length=254)
    nevers = models.ManyToManyField(
        'Never', verbose_name='Nevers',  related_name='nevers', blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Criado em')

    def __str__(self):
        return "#{}-{}".format(self.id, self.name)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
