# Generated by Django 4.2.2 on 2023-06-28 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_assetrequestmodel_delivery_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetrequestmodel',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]