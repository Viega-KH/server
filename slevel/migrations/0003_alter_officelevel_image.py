# Generated by Django 5.0.7 on 2024-08-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slevel', '0002_alter_infolevel_options_alter_officelevel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officelevel',
            name='image',
            field=models.ImageField(default='default/o1.jpg', upload_to='offis/', verbose_name='Фото'),
        ),
    ]
