# Generated by Django 5.0.7 on 2024-08-04 18:51

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_alter_news_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=markdownx.models.MarkdownxField(unique=True),
        ),
    ]
