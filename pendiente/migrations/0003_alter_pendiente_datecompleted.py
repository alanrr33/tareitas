# Generated by Django 3.2 on 2021-05-03 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendiente', '0002_rename_pendientes_pendiente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendiente',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
