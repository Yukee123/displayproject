# Generated by Django 4.0 on 2021-12-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displayapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_data',
            name='id',
        ),
        migrations.AlterField(
            model_name='student_data',
            name='usn',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
