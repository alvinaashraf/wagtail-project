# Generated by Django 5.0.2 on 2024-03-07 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_remove_postpageblogcategory_blog_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="postpage",
            name="description",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]