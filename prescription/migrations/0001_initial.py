# Generated by Django 4.1.4 on 2022-12-16 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription_patient', models.CharField(max_length=150)),
                ('prescription_doctor', models.CharField(max_length=150)),
            ],
        ),
    ]
