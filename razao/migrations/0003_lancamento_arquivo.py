# Generated by Django 4.1.1 on 2022-10-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razao', '0002_lancamento_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='lancamento',
            name='arquivo',
            field=models.FileField(blank=True, upload_to='arquivos/'),
        ),
    ]