# Generated by Django 4.1.4 on 2023-05-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='state',
        ),
        migrations.AddField(
            model_name='record',
            name='country',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
