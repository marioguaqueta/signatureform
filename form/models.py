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


class AuthDiscountRouster(models.Model):

    name = models.CharField(
        max_length = 50,
        verbose_name = 'Nombre',
        )

    identification = models.CharField(
        max_length = 50,
        verbose_name = 'Identificación',
        )

    signature = models.CharField(
        max_length=15000,
        null = True,
        blank = True,
        verbose_name = 'Firma'
        )

    code = models.CharField(
        max_length = 50,
        verbose_name = 'Codigo',
        )

    key = models.CharField(
        max_length = 50,
        verbose_name = 'Clave',
        )

    legal_rep = models.CharField(
        max_length = 50,
        verbose_name = 'Representante Legal',
        )

    nit = models.CharField(
        max_length = 50,
        verbose_name = 'Nit',
        )

    signature_rep = models.CharField(
        max_length=15000,
        null = True,
        blank = True,
        verbose_name = 'Firma Repesentante Legal'
        )



    def __str__(self):
        return (self.name + ' ' + self.identification)






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
