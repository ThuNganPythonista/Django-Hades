# Generated by Django 4.2.3 on 2023-08-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='color',
            field=models.CharField(choices=[('Yellow', 'mau vang'), ('Green', 'mau xanh')], default='Green', max_length=20),
        ),
    ]
