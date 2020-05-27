# Generated by Django 3.0 on 2020-04-09 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0006_auto_20200409_0539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('record_user_id', models.CharField(max_length=200)),
                ('record_time', models.DateTimeField(auto_now_add=True)),
                ('record_food', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['record_user_id', 'record_time'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_height', models.FloatField(default=0.0)),
                ('user_weight', models.FloatField(default=0.0)),
                ('user_sex', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], default='', max_length=6)),
            ],
            options={
                'ordering': ['user_name', 'user_id'],
            },
        ),
        migrations.DeleteModel(
            name='Food',
        ),
    ]