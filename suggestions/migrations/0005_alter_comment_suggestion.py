# Generated by Django 3.2.12 on 2022-06-08 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0004_alter_comment_suggestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='suggestion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='suggestions.suggestion'),
        ),
    ]
