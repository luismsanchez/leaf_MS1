# Generated by Django 3.2.7 on 2021-11-11 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarioApp', '0005_alter_comentario_calificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='calificacion',
            field=models.CharField(choices=[(0, '0'), (1, '★'), (2, '★ ★'), (3, '★ ★ ★'), (4, '★ ★ ★ ★'), (5, '★ ★ ★ ★ ★')], max_length=1),
        ),
    ]
