# Generated by Django 3.0.8 on 2020-08-16 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('objet_name', models.CharField(max_length=255)),
                ('email_id', models.CharField(max_length=101)),
                ('phone_num', models.CharField(max_length=15)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_title', models.CharField(max_length=100)),
                ('home_description', models.CharField(max_length=300)),
                ('home_image', models.ImageField(upload_to='home_img/')),
            ],
        ),
        migrations.CreateModel(
            name='Lois',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lois_title', models.CharField(max_length=300)),
                ('propostion_nom', models.CharField(max_length=300)),
                ('lois_content', models.TextField()),
                ('lois_image', models.ImageField(upload_to='lois_img/')),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReseauSociaux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rs_title', models.CharField(max_length=250)),
                ('rs_url', models.URLField()),
                ('rs_logo', models.ImageField(upload_to='socio_logo/')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now=True, null=True)),
                ('comment_title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lois', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='app.Lois')),
            ],
            options={
                'verbose_name': 'commentaire',
                'verbose_name_plural': 'commentaires',
            },
        ),
    ]