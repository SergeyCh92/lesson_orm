# Generated by Django 4.0.4 on 2022-04-16 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_remove_scope_is_main_tags_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels2', to='articles.scope'),
        ),
    ]