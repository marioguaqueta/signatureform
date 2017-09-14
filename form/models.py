from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):


    identification = models.CharField(
        max_length = 30,
        blank = True,
        null = True,
        verbose_name = 'Identificación',
        )

    identificationType = models.ForeignKey(
        'IdentificationType',
        blank = True,
        null = True,
        verbose_name = 'Tipo de Identificación',
        )

    phone = models.CharField(
        max_length = 30,
        blank = True,
        null = True,
        verbose_name = 'Teléfono',
        )

    city = models.ForeignKey(
        'Cities',
        blank = True,
        null = True,
        verbose_name = 'Ciudad',
        )

    address = models.CharField(
        max_length = 80,
        blank = True,
        null = True,
        verbose_name = 'Dirección',
        )

    birthDate = models.DateField(
        verbose_name='Fecha de nacimiento',
        blank=True,
        null=True,
        )

    gender = models.ForeignKey(
        'GenderType',
        null = True,
        blank = True,
        verbose_name = 'Género'
        )

    signature = models.ImageField(
        upload_to='icon/userSignature/',
        max_length=255,
        null = True,
        blank = True,
        help_text='300x300',
        verbose_name = 'Firma'
        )


    def __str__(self):
        return self.email





class GenderType(models.Model):
    
    name = models.CharField(
        max_length = 50,
        verbose_name = 'Género',
        )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Descripción',
        )


    def __str__(self):
        return self.name   



class IdentificationType(models.Model):
    """Models to set the id types allowed
    """
    name = models.CharField(
        max_length = 50,
        verbose_name = 'Tipo de identificación',
        )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=u'Descripción',
        )


    def __str__(self):
        return self.name


class Cities(models.Model):

    name = models.CharField(
        max_length=200, 
        verbose_name=u'Nombre',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Ciudad'
        verbose_name_plural = u'Ciudades'
