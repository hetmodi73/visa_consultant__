# Generated by Django 4.0.4 on 2022-05-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permanent_residence', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permanent_resi',
            name='QUALIFICATIONS_2',
            field=models.CharField(blank=True, choices=[('Recognised Canada qualification (and at least two years study in Canada) (10 Points)', 'Recognised Canada qualification (and at least two years study in Canada) (10 Points)'), ('Qualification in an identified future growth area, cluster or area of absolute skill shortage (5 Points)', 'Qualification in an identified future growth area, cluster or area of absolute skill shortage (5 Points)')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='permanent_resi',
            name='SKILLED_EMPLOYMENT',
            field=models.CharField(blank=True, choices=[('Current skilled employment in Canada for 12 months or more (60 Points)', 'Current skilled employment in Canada for 12 months or more (60 Points)'), ('Offer of skilled employment in Canada or current skilled employment in Canada for less than 12 months (50 Points)', 'Offer of skilled employment in Canada or current skilled employment in Canada for less than 12 months (50 Points)')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='permanent_resi',
            name='Skilled_employment_2',
            field=models.CharField(blank=True, choices=[('An identified future growth area, identified cluster, area of absolute skills shortage (5 Points)', 'An identified future growth area, identified cluster, area of absolute skills shortage (5 Points)'), ('Region outside Canada (10 Points)', 'Region outside Auckland (10 Points)'), ('Partner employment or offer of employment (10 Points)', 'Partner employment or offer of employment (10 Points)')], max_length=200, null=True),
        ),
    ]