# Generated by Django 4.2.11 on 2024-03-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_content_blog_published_on_alter_blog_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(default='The main content of your post goes here'),
        ),
    ]
