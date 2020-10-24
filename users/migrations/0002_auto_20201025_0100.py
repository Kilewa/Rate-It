# Generated by Django 3.1.2 on 2020-10-24 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import url_or_relative_url_field.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='profile_photo',
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=url_or_relative_url_field.fields.URLOrRelativeURLField(default=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=tinymce.models.HTMLField(default='No bio', max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
