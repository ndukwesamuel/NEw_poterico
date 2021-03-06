# Generated by Django 3.1.1 on 2021-01-01 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('status', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('S', 'Shirt'), ('SW', 'SportWear'), ('OW', 'OutWear')], max_length=2)),
                ('label', models.CharField(choices=[('S', 'secondary'), ('P', 'primary'), ('D', 'danger')], max_length=2)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='productImages')),
            ],
        ),
    ]
