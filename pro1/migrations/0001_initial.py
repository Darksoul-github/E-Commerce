# Generated by Django 3.0.6 on 2020-07-14 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SpecCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcat_name', models.CharField(max_length=20)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro1.Category')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcat_name', models.CharField(max_length=20)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro1.SubCategory1')),
            ],
        ),
        migrations.CreateModel(
            name='SpecProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.CharField(max_length=20)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro1.SpecCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('img', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=1000)),
                ('Quantity', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro1.Category')),
                ('spec_property', models.ManyToManyField(to='pro1.SpecProperty')),
                ('sub_cat1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro1.SubCategory1')),
                ('sub_cat2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pro1.SubCategory2')),
            ],
        ),
    ]