# Generated by Django 3.1.4 on 2022-04-01 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20220401_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]