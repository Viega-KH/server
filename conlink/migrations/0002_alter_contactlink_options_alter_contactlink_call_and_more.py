# Generated by Django 5.0.7 on 2024-08-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conlink', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactlink',
            options={'verbose_name': 'связь', 'verbose_name_plural': 'связь'},
        ),
        migrations.AlterField(
            model_name='contactlink',
            name='call',
            field=models.CharField(max_length=15, null=True, verbose_name='телефон'),
        ),
        migrations.AlterField(
            model_name='contactlink',
            name='email',
            field=models.EmailField(max_length=200, null=True, verbose_name='эмаль'),
        ),
        migrations.AlterField(
            model_name='contactlink',
            name='facebook',
            field=models.URLField(null=True, verbose_name='Фейсбук'),
        ),
        migrations.AlterField(
            model_name='contactlink',
            name='instagram',
            field=models.URLField(null=True, verbose_name='инстаграм'),
        ),
        migrations.AlterField(
            model_name='contactlink',
            name='location',
            field=models.CharField(max_length=200, null=True, verbose_name='расположение'),
        ),
        migrations.AlterField(
            model_name='contactlink',
            name='telegram',
            field=models.URLField(null=True, verbose_name='телеграмма'),
        ),
        migrations.AlterField(
            model_name='contactlink',
            name='twitter',
            field=models.URLField(null=True, verbose_name='Твиттер'),
        ),
    ]
