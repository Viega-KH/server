# Generated by Django 5.0.7 on 2024-08-04 18:27

import django_summernote.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_news_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=django_summernote.fields.SummernoteTextField(verbose_name='мазмун'),
        ),
    ]
