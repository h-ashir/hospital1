# Generated by Django 4.1.7 on 2023-10-16 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=100)),
                ('doc_spec', models.CharField(max_length=100)),
                ('doc_image', models.ImageField(upload_to='doctors')),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.department')),
            ],
        ),
    ]
