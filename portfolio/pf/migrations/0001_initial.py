# Generated by Django 3.1.7 on 2021-04-19 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogName', models.TextField(help_text='Name for the blog', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagoryName', models.TextField(help_text='Name for catagory', max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(help_text='Title of the message', max_length=100)),
                ('content', models.TextField(help_text='Content of the message', max_length=500)),
                ('datePublished', models.DateTimeField()),
                ('image', models.ImageField(height_field='height', upload_to='images', width_field='width')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='pf.blog')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='catagories',
            field=models.ManyToManyField(help_text='Catagories relevant to blog being created.', to='pf.Catagory'),
        ),
    ]
