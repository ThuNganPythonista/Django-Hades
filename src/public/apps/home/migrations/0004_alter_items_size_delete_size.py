# Generated by Django 4.2.3 on 2023-11-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_items_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='size',
            field=models.CharField(default=10, max_length=5),
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]