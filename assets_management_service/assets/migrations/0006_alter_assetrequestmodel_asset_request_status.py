# Generated by Django 4.2.2 on 2023-06-30 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_assetrequestmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetrequestmodel',
            name='asset_request_status',
            field=models.CharField(choices=[('COMPLETED', 'Completed'), ('IN_PROGRESS', 'In_Progress'), ('RETURNED_INITIATED', 'Return_Initiated'), ('WAITING_FOR_APPROVAL', 'Waiting_For_Approval'), ('WAITING_FOR_RENEWAL_APPROVAL', 'Waiting_For_Renewal_Approval')], default='Waiting_For_Approval', max_length=45),
        ),
    ]