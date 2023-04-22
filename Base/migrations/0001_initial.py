# Generated by Django 4.1.7 on 2023-04-21 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=150)),
                ('fechaComentario', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Diseño',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('diseño', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=500)),
                ('fechaPost', models.DateField()),
                ('emailUsuario', models.EmailField(max_length=50)),
            ],
        ),
    ]
