# Generated by Django 4.0.4 on 2022-05-05 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_alter_user_address_alter_user_email_id_and_more'),
        ('services', '0003_alter_service_service_name_delete_service_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='client.user'),
        ),
        migrations.AlterField(
            model_name='service',
            name='SERVICE_NAME',
            field=models.CharField(blank=True, choices=[('IELTS Inquiry', 'IELTS Inquiry'), ('Immigration Visa', 'Immigration Visa'), ('Non-Immigration Visa', 'Non-Immigration Visa'), ('Visitor Visa', 'Visitor Visa'), ('Student Visa', 'Student Visa'), ('Business Visa', 'Business Visa'), ('Permanent Residence', 'Permanent Residence')], max_length=25, null=True),
        ),
    ]