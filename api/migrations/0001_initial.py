# Generated by Django 4.0.5 on 2022-06-25 10:09

import api.utils
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('source', models.PositiveSmallIntegerField(choices=[(1, 'Upload'), (2, 'Remote')], default=1)),
                ('source_path', models.URLField(blank=True, null=True)),
                ('original_file', models.ImageField(max_length=255, upload_to=api.utils.image_upload_path)),
                ('transformed_file', models.ImageField(blank=True, max_length=255, null=True, upload_to=api.utils.image_upload_path)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'upload_image',
            },
        ),
        migrations.CreateModel(
            name='UploadRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('images', models.ManyToManyField(related_name='upload_request', to='api.uploadimage')),
            ],
            options={
                'db_table': 'upload_request',
            },
        ),
    ]
