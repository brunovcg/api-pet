# Generated by Django 3.2.8 on 2021-10-27 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
        ('characteristic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.FloatField()),
                ('weight', models.FloatField()),
                ('sex', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalCharacteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.animal')),
                ('characteristic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characteristic.characteristic')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='characteristics',
            field=models.ManyToManyField(related_name='animal', through='animal.AnimalCharacteristic', to='characteristic.Characteristic'),
        ),
        migrations.AddField(
            model_name='animal',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal', to='group.group'),
        ),
    ]