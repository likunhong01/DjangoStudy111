# Generated by Django 2.1.5 on 2019-02-19 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='password',
            field=models.CharField(default=123, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=32),
        ),
    ]
