# Generated by Django 3.2.5 on 2022-03-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary_main', '0002_alter_comment_c_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='c_author',
            field=models.CharField(max_length=30),
        ),
    ]
