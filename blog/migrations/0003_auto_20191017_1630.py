# Generated by Django 2.2.6 on 2019-10-17 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20191016_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='author',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='text',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='title',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='create_date',
        ),
        migrations.AddField(
            model_name='chat',
            name='name',
            field=models.CharField(default='hey you', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Chat'),
        ),
    ]
