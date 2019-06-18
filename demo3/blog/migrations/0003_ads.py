# Generated by Django 2.2.2 on 2019-06-17 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='ads')),
                ('desc', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=20)),
            ],
        ),
    ]
