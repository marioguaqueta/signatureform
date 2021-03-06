# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_user_signature'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthDiscountRouster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('identification', models.CharField(max_length=50, verbose_name='Identificación')),
                ('signature', models.ImageField(blank=True, help_text='300x300', max_length=255, null=True, upload_to='icon/userSignature/', verbose_name='Firma')),
                ('code', models.CharField(max_length=50, verbose_name='Codigo')),
                ('key', models.CharField(max_length=50, verbose_name='Clave')),
                ('legal_rep', models.CharField(max_length=50, verbose_name='Representante Legal')),
                ('nit', models.CharField(max_length=50, verbose_name='Nit')),
                ('signature_rep', models.ImageField(blank=True, help_text='300x300', max_length=255, null=True, upload_to='icon/userSignature/', verbose_name='Firma Repesentante Legal')),
            ],
        ),
    ]
