# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 16:46
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blocks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('max_score', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
            },
        ),
        migrations.CreateModel(
            name='TaskResultBlockResultRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Связь результата здания с результатом блока',
            },
        ),
        migrations.CreateModel(
            name='BlockResult',
            fields=[
                ('result_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='results.Result')),
            ],
            options={
                'verbose_name': 'Результат ответа на блок',
                'verbose_name_plural': 'Результаты ответов на блоки',
            },
            bases=('results.result',),
        ),
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('result_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='results.Result')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task', verbose_name='Урок')),
            ],
            options={
                'verbose_name': 'Результат урока',
                'verbose_name_plural': 'Результаты уроков',
            },
            bases=('results.result',),
        ),
        migrations.AddField(
            model_name='result',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ученик'),
        ),
        migrations.CreateModel(
            name='ChoiceBlockResult',
            fields=[
                ('blockresult_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='results.BlockResult')),
                ('choices', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
            options={
                'verbose_name': 'Результат ответа на тестовый вопрос',
                'verbose_name_plural': 'Результаты ответов на тестовые вопросы',
            },
            bases=('results.blockresult',),
        ),
        migrations.CreateModel(
            name='FloatBlockResult',
            fields=[
                ('blockresult_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='results.BlockResult')),
                ('answer', models.FloatField(verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Результат ответа на задачу',
                'verbose_name_plural': 'Результаты ответов на задачи',
            },
            bases=('results.blockresult',),
        ),
        migrations.CreateModel(
            name='TextAnswerBlockResult',
            fields=[
                ('blockresult_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='results.BlockResult')),
                ('correct_answers', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
            ],
            options={
                'verbose_name': 'Результат ответа на задание с текстовым ответом',
                'verbose_name_plural': 'Результаты ответов на задание с текстовым ответом',
            },
            bases=('results.blockresult',),
        ),
        migrations.AddField(
            model_name='taskresultblockresultrelation',
            name='block_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.BlockResult'),
        ),
        migrations.AddField(
            model_name='taskresultblockresultrelation',
            name='task_result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.TaskResult'),
        ),
        migrations.AddField(
            model_name='blockresult',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blocks.Block'),
        ),
    ]
