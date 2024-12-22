# Generated by Django 5.1.4 on 2024-12-22 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('F', 'Fruit'), ('V', 'vegetable'), ('M', 'Meat'), ('O', 'Other')], max_length=1)),
            ],
        ),
    ]
