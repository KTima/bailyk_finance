# Generated by Django 3.2.7 on 2022-03-21 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankcards', '0003_alter_typecard_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddata',
            name='Numbers',
            field=models.BigIntegerField(default=0, unique=True, verbose_name='Номер карты'),
        ),
    ]