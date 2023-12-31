# Generated by Django 4.1.7 on 2023-07-07 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('mailid', models.CharField(max_length=255)),
                ('address', models.TextField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
                ('purpose', models.CharField(max_length=255)),
                ('meterialprovide', models.CharField(max_length=255)),
            ],
        ),
    ]
