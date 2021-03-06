# Generated by Django 2.2.12 on 2022-05-02 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bathroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default='A Bathroom', help_text='Enter the bathroom location (e.g. Elmhurst Park Bathroom)', max_length=1000)),
                ('building', models.IntegerField(help_text='What floor is the bathroom on?', max_length=100)),
                ('size', models.IntegerField(help_text='Enter how many stalls there are', max_length=10)),
                ('cleanliness', models.IntegerField(default=5, help_text='Rate the cleanliness of the bathroom on a scale of 1 to 10', max_length=10)),
                ('bathNum', models.IntegerField(default=1000, help_text='Enter the bathroomID', max_length=1000)),
            ],
            options={
                'ordering': ['location', '-size', '-cleanliness'],
            },
        ),
    ]
