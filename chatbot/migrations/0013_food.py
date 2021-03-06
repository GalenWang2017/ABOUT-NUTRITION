# Generated by Django 3.0 on 2020-04-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0012_remove_recipe_recipe_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_id', models.AutoField(primary_key=True, serialize=False)),
                ('food_name', models.CharField(max_length=100)),
                ('food_power', models.FloatField(blank=True, default=0.0)),
                ('food_protein', models.FloatField(blank=True, default=0.0)),
                ('food_carbohydrate', models.FloatField(blank=True, default=0.0)),
                ('food_fat', models.FloatField(blank=True, default=0.0)),
            ],
        ),
    ]
