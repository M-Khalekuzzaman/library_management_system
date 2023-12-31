# Generated by Django 4.2.3 on 2023-09-30 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookBorrowModel',
            fields=[
                ('isbn_number', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('Harry-Poter', 'Harry-Poter'), ('Drama', 'Drama'), ('Sci-Fi', 'Sci-Fi'), ('Horror', 'Horror')], max_length=30)),
                ('availability', models.IntegerField()),
                ('first_pub', models.DateTimeField(auto_now_add=True)),
                ('last_pub', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
