# Generated by Django 2.2.5 on 2019-11-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0006_auto_20191121_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
