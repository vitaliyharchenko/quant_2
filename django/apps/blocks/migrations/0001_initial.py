# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nodes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(blank=True, verbose_name='Время в минутах на выполнение блока')),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceBlockOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_text', models.CharField(blank=True, max_length=600, verbose_name='Вариант ответа')),
                ('option_image', models.ImageField(blank=True, null=True, upload_to='choice_block_options/', verbose_name='Картинка')),
                ('help_text', models.CharField(blank=True, max_length=300, verbose_name='Подсказка')),
                ('is_true', models.BooleanField(verbose_name='Правильный?')),
            ],
            options={
                'verbose_name': 'Вариант ответа на тестовый вопрос',
                'verbose_name_plural': 'Варианты ответа на тестовые вопросы',
            },
        ),
        migrations.CreateModel(
            name='NodeBlockRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'включение блока в узел',
                'verbose_name_plural': 'включения блоков в узел',
            },
        ),
        migrations.CreateModel(
            name='ChoiceBlock',
            fields=[
                ('block_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blocks.Block')),
                ('question_text', models.CharField(max_length=600, verbose_name='Текст вопроса')),
                ('image', models.ImageField(blank=True, null=True, upload_to='choice_blocks/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'тестовый вопрос',
                'verbose_name_plural': 'тестовые вопросы',
            },
            bases=('blocks.block',),
        ),
        migrations.CreateModel(
            name='FloatBlock',
            fields=[
                ('block_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blocks.Block')),
                ('question_text', models.CharField(max_length=600, verbose_name='Текст вопроса')),
                ('image', models.ImageField(blank=True, null=True, upload_to='float_questions/', verbose_name='Картинка')),
                ('answer', models.FloatField(verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'задача с численным ответом',
                'verbose_name_plural': 'задачи с численным ответом',
            },
            bases=('blocks.block',),
        ),
        migrations.CreateModel(
            name='TextAnswerBlock',
            fields=[
                ('block_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blocks.Block')),
                ('question_text', models.CharField(max_length=600, verbose_name='Текст вопроса')),
                ('image', models.ImageField(blank=True, null=True, upload_to='float_questions/', verbose_name='Картинка')),
                ('answer', models.CharField(max_length=600, verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'задача с текстовым ответом',
                'verbose_name_plural': 'задачи с текстовым ответом',
            },
            bases=('blocks.block',),
        ),
        migrations.CreateModel(
            name='TextBlock',
            fields=[
                ('block_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blocks.Block')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('body', models.CharField(max_length=600)),
            ],
            options={
                'verbose_name': 'текстовая статья',
                'verbose_name_plural': 'текстовые статьи',
            },
            bases=('blocks.block',),
        ),
        migrations.AddField(
            model_name='nodeblockrelation',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blocks.Block'),
        ),
        migrations.AddField(
            model_name='nodeblockrelation',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodes.Node'),
        ),
        migrations.AddField(
            model_name='choiceblockoption',
            name='choice_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blocks.ChoiceBlock'),
        ),
    ]