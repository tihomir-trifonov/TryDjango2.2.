# Generated by Django 2.2 on 2020-09-28 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200928_2304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-timestamp', '-updated']},
        ),
    ]