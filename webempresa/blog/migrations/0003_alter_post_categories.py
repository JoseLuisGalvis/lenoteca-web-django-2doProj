# Generated by Django 4.1.2 on 2023-03-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_categories_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='blog.category', verbose_name='Categorías'),
        ),
    ]
