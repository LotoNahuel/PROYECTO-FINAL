# Generated by Django 4.1.7 on 2023-04-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_alter_diseño_fechapost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseño',
            name='fechaPost',
            field=models.DateField(),
        ),
    ]
