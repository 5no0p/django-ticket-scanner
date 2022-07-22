# Generated by Django 3.2.7 on 2021-09-23 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('amount_of_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('F', 'Full Paid'), ('N', 'Not Paid'), ('S', 'Semi Paid')], max_length=1)),
                ('screenshot', models.ImageField(upload_to='payment/screenshots/')),
                ('purchased_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_info', to='ticket.ticket')),
            ],
        ),
    ]
