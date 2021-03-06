# Generated by Django 4.0.4 on 2022-05-05 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0009_alter_user_address_alter_user_email_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='permanent_resi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKILLED_EMPLOYMENT', models.CharField(blank=True, choices=[('Current skilled employment in New Zealand for 12 months or more (60 Points)', 'Current skilled employment in New Zealand for 12 months or more (60 Points)'), ('Offer of skilled employment in New Zealand or current skilled employment in New Zealand for less than 12 months (50 Points)', 'Offer of skilled employment in New Zealand or current skilled employment in New Zealand for less than 12 months (50 Points)')], max_length=200, null=True)),
                ('WORK_EXPERIENCE', models.CharField(blank=True, choices=[('2 Years (10 Points)', '2 Years (10 Points)'), ('4 Years (15 Points)', '4 Years (15 Points)'), ('6 Years (20 Points)', '6 Years (20 Points)'), ('8 Years (25 Points)', '8 Years (25 Points)'), ('10 Years (30 Points)', '10 Years (30 Points)')], max_length=200, null=True)),
                ('QUALIFICATIONS', models.CharField(blank=True, choices=[('Recognised basic qualification (e.g. trade qualification, diploma, bachelors degree, bachelors degree with Honours) (50 Points)', 'Recognised basic qualification (e.g. trade qualification, diploma, bachelors degree, bachelors degree with Honours) (50 Points)'), ('Recognised post-graduate qualification (Masters degree, Doctorate) (55 Points)', 'Recognised post-graduate qualification (Masters degree, Doctorate) (55 Points)')], max_length=200, null=True)),
                ('AGE_20TO55_YEARS', models.CharField(blank=True, choices=[('20-29 (30 Points)', '20-29 (30 Points)'), ('30-39 (25 Points)', '30-39 (25 Points)'), ('40-44 (20 Points)', '40-44 (20 Points)'), ('45-49 (10 Points)', '45-49 (10 Points)'), ('50-55 (5 Points)', '50-55 (5 Points)')], max_length=200, null=True)),
                ('Skilled_employment_2', models.CharField(blank=True, choices=[('An identified future growth area, identified cluster, area of absolute skills shortage (5 Points)', 'An identified future growth area, identified cluster, area of absolute skills shortage (5 Points)'), ('Region outside Auckland (10 Points)', 'Region outside Auckland (10 Points)'), ('Partner employment or offer of employment (10 Points)', 'Partner employment or offer of employment (10 Points)')], max_length=200, null=True)),
                ('Work_experience_2', models.CharField(blank=True, choices=[('2 Years (5 Points)', '2 Years (5 Points)'), ('4 Years (10 Points)', '4 Years (10 Points)'), ('6 Years (15 Points)', '6 Years (15 Points)')], max_length=200, null=True)),
                ('Additional_Bonus_Points', models.CharField(blank=True, choices=[('2 to 5 years (5 Points)', '2 to 5 years (5 Points)'), ('6 years or more (10 Points)', '6 years or more (10 Points)')], max_length=200, null=True)),
                ('QUALIFICATIONS_2', models.CharField(blank=True, choices=[('Recognised New Zealand qualification (and at least two years study in NZ) (10 Points)', 'Recognised New Zealand qualification (and at least two years study in NZ) (10 Points)'), ('Qualification in an identified future growth area, cluster or area of absolute skill shortage (5 Points)', 'Qualification in an identified future growth area, cluster or area of absolute skill shortage (5 Points)')], max_length=200, null=True)),
                ('Partner_Qualifications', models.CharField(blank=True, choices=[('None', 'None'), ('Partner Qualifications (10 Points)', 'Partner Qualifications (10 Points)')], max_length=200, null=True)),
                ('text', models.TextField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('resume', models.FileField(blank=True, default='', null=True, upload_to='profile')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permanent_resi', to='client.user')),
            ],
        ),
    ]
