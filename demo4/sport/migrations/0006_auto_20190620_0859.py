# Generated by Django 2.2.2 on 2019-06-20 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0005_subject_matter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Style',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
