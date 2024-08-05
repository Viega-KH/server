# Generated by Django 5.0.7 on 2024-08-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'последнее', 'verbose_name_plural': 'последнее'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='время'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='full_name',
            field=models.CharField(max_length=200, verbose_name='полное имя'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='содержание'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='телефон'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='published_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='время'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='заголовок'),
        ),
    ]
