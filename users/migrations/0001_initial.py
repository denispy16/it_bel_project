# Generated by Django 4.2.2 on 2023-07-03 12:06

from django.db import migrations, models
import django.utils.timezone
import users.managers.user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID автора')),
                ('author_name', models.CharField(blank=True, max_length=150, unique=True, verbose_name='Ник автора')),
                ('name', models.CharField(max_length=150, verbose_name='Имя автора')),
                ('surname', models.CharField(max_length=150, verbose_name='Фамилия автора')),
                ('age', models.IntegerField(help_text='Возраст', verbose_name='Возраст автора')),
                ('email', models.EmailField(help_text='Email', max_length=254, verbose_name='Почта автора')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата регистрации')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активный')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID пользователя')),
                ('username', models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='Имя пользователя')),
                ('email', models.EmailField(help_text='Email', max_length=254, unique=True, verbose_name='Почта пользователя')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата регистрации')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Админ')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Супер')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', users.managers.user.UserManager()),
            ],
        ),
    ]