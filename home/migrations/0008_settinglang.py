# Generated by Django 3.0.6 on 2020-05-31 01:32

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_faq_lang'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingLang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(choices=[('en', 'English'), ('tr', 'Türkçe'), ('ru', 'Pусский'), ('hi', 'हिंदी द्वारा')], max_length=6)),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('aboutus', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('references', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Setting')),
            ],
        ),
    ]