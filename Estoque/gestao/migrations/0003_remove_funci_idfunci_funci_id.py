# Generated by Django 4.2.4 on 2023-10-11 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0002_estoque_pronome_estoque_quanesto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funci',
            name='idFunci',
        ),
        migrations.AddField(
            model_name='funci',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]