# Generated by Django 4.1.4 on 2023-02-22 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.commonmodel')),
                ('caption', models.CharField(max_length=150)),
            ],
            bases=('common.commonmodel',),
        ),
    ]
