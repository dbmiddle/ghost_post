# Generated by Django 3.0.6 on 2020-05-15 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gposts', '0010_auto_20200515_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boastsandroasts',
            name='content',
            field=models.CharField(max_length=500),
        ),
    ]
