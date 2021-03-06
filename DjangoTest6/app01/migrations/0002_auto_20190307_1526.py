# Generated by Django 2.1.5 on 2019-03-07 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=32, verbose_name='用户名'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='u2g',
            field=models.ManyToManyField(to='app01.UserGroup'),
        ),
    ]
