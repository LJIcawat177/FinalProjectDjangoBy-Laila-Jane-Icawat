# Generated by Django 5.1.1 on 2024-12-01 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodrecipe',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodblog.foodcategories'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='food_images/')),
                ('description', models.TextField()),
                ('recipe', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodblog.foodcategories')),
            ],
        ),
    ]
