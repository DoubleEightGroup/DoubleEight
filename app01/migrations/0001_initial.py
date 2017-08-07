# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('up_count', models.IntegerField()),
                ('down_count', models.IntegerField()),
                ('read_count', models.IntegerField()),
                ('edit_count', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ccont', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Article')),
            ],
        ),
        migrations.CreateModel(
            name='UpDown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.IntegerField(choices=[(0, '踩'), (1, '赞')])),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('nickname', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='updown',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Userinfo'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Userinfo'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Userinfo'),
        ),
        migrations.AlterUniqueTogether(
            name='updown',
            unique_together=set([('user', 'article')]),
        ),
    ]
