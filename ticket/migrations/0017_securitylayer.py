# Generated by Django 3.2.9 on 2022-07-23 13:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0016_auto_20220722_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityLayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('order', models.PositiveSmallIntegerField()),
                ('members', models.ManyToManyField(related_name='security', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
