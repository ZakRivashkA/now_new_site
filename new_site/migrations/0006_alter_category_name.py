# Generated by Django 4.0.4 on 2022-05-08 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_site', '0005_alter_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
