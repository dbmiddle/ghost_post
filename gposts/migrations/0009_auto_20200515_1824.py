# Generated by Django 3.0.6 on 2020-05-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gposts', '0008_auto_20200515_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boastsandroasts',
            name='is_boast',
            field=models.BooleanField(default=False),
        ),
    ]
