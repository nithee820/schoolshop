# Generated by Django 4.1.7 on 2023-07-07 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_student_students'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Students',
        ),
    ]
