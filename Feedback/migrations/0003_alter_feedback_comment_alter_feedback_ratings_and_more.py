# Generated by Django 4.0.4 on 2022-05-05 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_alter_user_address_alter_user_email_id_and_more'),
        ('Feedback', '0002_rename_l_id_feedback_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='COMMENT',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='RATINGS',
            field=models.CharField(blank=True, choices=[('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3'), ('3.5', '3.5'), ('4', '4'), ('4.5', '4.5'), ('5', '5')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='client.user'),
        ),
    ]