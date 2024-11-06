# Generated by Django 3.2.4 on 2023-12-01 23:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('startScan', '0056_alter_endpoint_techs'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanhistory',
            name='aborted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aborted_scans', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='scanhistory',
            name='initiated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='initiated_scans', to=settings.AUTH_USER_MODEL),
        ),
    ]
