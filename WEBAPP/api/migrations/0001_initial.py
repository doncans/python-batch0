# Generated by Django 3.2.2 on 2021-05-19 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=200)),
                ('emp_sal', models.CharField(max_length=200)),
                ('emp_design', models.CharField(max_length=200)),
            ],
        ),
    ]
