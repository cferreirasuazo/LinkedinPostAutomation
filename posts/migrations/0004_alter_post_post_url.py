# Generated by Django 4.0.6 on 2022-08-04 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_post_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_url',
            field=models.TextField(default=None, null=True),
        ),
    ]