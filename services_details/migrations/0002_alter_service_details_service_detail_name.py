# Generated by Django 4.0.4 on 2022-05-05 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_details',
            name='SERVICE_DETAIL_NAME',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]