# Generated by Django 2.1.4 on 2018-12-08 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantencion', '0003_auto_20181208_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formatrabajo',
            name='numasc',
            field=models.IntegerField(),
        ),
    ]
