# Generated by Django 4.0.4 on 2022-04-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_scope_articles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='is_main',
        ),
        migrations.AddField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
    ]
