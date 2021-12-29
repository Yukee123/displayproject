# Generated by Django 4.0 on 2021-12-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usn', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default=None, max_length=6)),
                ('course', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Student_Data',
                'verbose_name_plural': 'Student_Datas',
            },
        ),
    ]
