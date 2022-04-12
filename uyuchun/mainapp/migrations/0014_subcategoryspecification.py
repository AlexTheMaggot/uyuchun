# Generated by Django 4.0.3 on 2022-04-12 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_rename_productspecifications_productspecification'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategorySpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategoryspecification', to='mainapp.specification')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategoryspecification', to='mainapp.subcategory')),
            ],
        ),
    ]
