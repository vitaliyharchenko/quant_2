# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-09 07:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGroupRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('finish_time', models.DateTimeField(blank=True, null=True)),
                ('is_finished', models.BooleanField(default=False, verbose_name='Закончили?')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
            options={
                'verbose_name': 'связь группы и курса',
                'verbose_name_plural': 'связи групп и курсов',
            },
        ),
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название группы')),
                ('about', models.TextField(verbose_name='Описание группы')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'группа',
                'verbose_name_plural': 'группа',
            },
        ),
        migrations.CreateModel(
            name='StudentGroupRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.StudentGroup')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'связь ученика с группой',
                'verbose_name_plural': 'связи учеников с группой',
            },
        ),
        migrations.AddField(
            model_name='coursegrouprelation',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.StudentGroup'),
        ),
    ]