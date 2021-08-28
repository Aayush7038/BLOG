# Generated by Django 3.2.4 on 2021-06-24 08:34

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(blank=True, upload_to='videosimages')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=200)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('desc', models.TextField()),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.categorylist')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
