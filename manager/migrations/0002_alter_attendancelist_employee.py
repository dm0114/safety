# Generated by Django 3.2.12 on 2022-06-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancelist',
            name='employee',
            field=models.CharField(max_length=15, verbose_name='근로자'),
        ),
    ]
