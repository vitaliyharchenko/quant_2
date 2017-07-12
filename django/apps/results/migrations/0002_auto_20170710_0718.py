# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 07:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blockresult',
            options={'verbose_name': 'результат ответа на блок', 'verbose_name_plural': 'результаты ответов на блоки'},
        ),
        migrations.AlterModelOptions(
            name='choiceblockresult',
            options={'verbose_name': 'результат ответа на тестовый вопрос', 'verbose_name_plural': 'результаты ответов на тестовые вопросы'},
        ),
        migrations.AlterModelOptions(
            name='floatblockresult',
            options={'verbose_name': 'результат ответа на задачу', 'verbose_name_plural': 'результаты ответов на задачи'},
        ),
        migrations.AlterModelOptions(
            name='result',
            options={'verbose_name': 'результат', 'verbose_name_plural': 'результаты'},
        ),
        migrations.AlterModelOptions(
            name='taskresult',
            options={'verbose_name': 'результат задания', 'verbose_name_plural': 'результаты заданий'},
        ),
        migrations.AlterModelOptions(
            name='taskresultblockresultrelation',
            options={'verbose_name': 'связь результата задания с результатом блока'},
        ),
        migrations.AlterModelOptions(
            name='textanswerblockresult',
            options={'verbose_name': 'результат ответа на задание с текстовым ответом', 'verbose_name_plural': 'результаты ответов на задание с текстовым ответом'},
        ),
    ]