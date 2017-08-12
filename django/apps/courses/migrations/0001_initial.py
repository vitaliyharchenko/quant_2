# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-09 07:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lessons', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0002_auto_20170809_0752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название курса')),
                ('about', models.TextField(verbose_name='Описание курса')),
                ('subject_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tags.SubjectTag')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='CourseLessonRelaion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='Порядковый номер урока в курсе')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.Lesson')),
            ],
            options={
                'verbose_name': 'включение урока в курс',
                'verbose_name_plural': 'включения урока в курс',
            },
        ),
    ]