# Generated by Django 4.2.2 on 2023-07-03 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID комментария')),
                ('text', models.TextField(max_length=300, verbose_name='Текст комментария')),
                ('added', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарий',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(help_text='Уникальный идентификатор новости', primary_key=True, serialize=False, verbose_name='ID книги')),
                ('title', models.CharField(help_text='Заголовок новости', max_length=50, verbose_name='Заголовок новости')),
                ('description', models.TextField(blank=True, max_length=25, null=True, verbose_name='Описание новости')),
                ('content', models.TextField(help_text='Содержание', verbose_name='Содержание')),
                ('cover', models.ImageField(help_text='Фотографии', upload_to='covers/', verbose_name='Фото')),
                ('added', models.DateTimeField(default=django.utils.timezone.now, help_text='Дата', verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
