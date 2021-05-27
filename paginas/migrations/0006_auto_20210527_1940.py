# Generated by Django 3.2.3 on 2021-05-27 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0005_alter_projeto_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
