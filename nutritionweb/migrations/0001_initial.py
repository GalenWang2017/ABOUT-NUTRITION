# Generated by Django 3.0 on 2020-04-09 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lineUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20)),
                ('userGender', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], default='Male', max_length=20)),
                ('userWeight', models.IntegerField()),
                ('userHeight', models.IntegerField()),
                ('userAge', models.IntegerField()),
                ('userId', models.CharField(max_length=256)),
            ],
        ),
    ]
