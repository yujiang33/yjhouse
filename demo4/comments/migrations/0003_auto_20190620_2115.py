# Generated by Django 2.2.2 on 2019-06-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20190620_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=20, verbose_name='姓名'),
        ),
    ]