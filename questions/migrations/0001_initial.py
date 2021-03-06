# Generated by Django 4.0.4 on 2022-05-03 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services_details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='master_question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QUESTION', models.CharField(max_length=50)),
                ('ANSWER', models.CharField(max_length=50)),
                ('POINTS', models.IntegerField()),
                ('services', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master_question', to='services_details.service_details')),
            ],
        ),
    ]
