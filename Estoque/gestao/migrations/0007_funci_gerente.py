# Generated by Django 4.2.4 on 2023-11-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0006_alter_funci_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='funci',
            name='gerente',
            field=models.BooleanField(default=False),
        ),
    ]
