# Generated by Django 3.2.5 on 2022-03-03 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary_main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='b_image',
            new_name='b_img',
        ),
    ]