# Generated by Django 3.2.3 on 2021-05-23 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0003_projeto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
