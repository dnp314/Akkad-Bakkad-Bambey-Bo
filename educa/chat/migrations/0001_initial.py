# Generated by Django 5.0.12 on 2025-03-09 10:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0004_course_students'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('sent_on', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chat_messages', to='courses.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chat_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
