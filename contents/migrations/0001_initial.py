# Generated by Django 4.2.2 on 2023-06-20 10:09

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('text', models.TextField(verbose_name='post text')),
                ('publish_at', models.DateTimeField(auto_now_add=True, verbose_name='publish at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user', verbose_name='User')),
            ],
            bases=(core.models.TimStampMixin, 'core.basemodel'),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50, verbose_name='Tag')),
                ('related_post', models.ManyToManyField(related_name='Tags', to='contents.post', verbose_name='Post')),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('related_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.post', verbose_name='Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user', verbose_name='user')),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='post-images', verbose_name='Image')),
                ('related_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='contents.post', verbose_name='post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('related_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.post', verbose_name='Post')),
                ('reply_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.comment', verbose_name='comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user', verbose_name='user')),
            ],
        ),
    ]