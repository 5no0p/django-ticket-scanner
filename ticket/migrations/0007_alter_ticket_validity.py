# Generated by Django 3.2.7 on 2021-09-28 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_auto_20210927_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='validity',
            field=models.BooleanField(default=True),
        ),
    ]
