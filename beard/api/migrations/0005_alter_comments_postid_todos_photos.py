# Generated by Django 4.0.3 on 2022-03-26 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_albums'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='postId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='api.posts'),
        ),
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('completed', models.BooleanField()),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='api.posts')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('thumbnailUrl', models.CharField(max_length=100)),
                ('albumId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='photos', to='api.albums')),
            ],
        ),
    ]