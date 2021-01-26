# Generated by Django 3.1.5 on 2021-01-23 16:33

from django.conf import settings
import django.contrib.auth.models
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imei_numbers',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('ImeiNumber', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone_brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectId', models.CharField(max_length=100, unique=True)),
                ('Model', models.CharField(max_length=100)),
                ('Brand', models.CharField(max_length=100)),
                ('Network', models.CharField(max_length=100)),
                ('TwoG', models.CharField(max_length=100)),
                ('ThreeG', models.CharField(max_length=100)),
                ('FourG', models.CharField(max_length=100)),
                ('Network_Speed', models.CharField(max_length=100)),
                ('GPRS', models.CharField(max_length=100)),
                ('EDGE', models.CharField(max_length=100)),
                ('Announced', models.CharField(max_length=100)),
                ('Status', models.CharField(max_length=100)),
                ('Dimensions', models.CharField(max_length=100)),
                ('field13', models.CharField(max_length=100)),
                ('SIM', models.CharField(max_length=100)),
                ('Display_type', models.CharField(max_length=100)),
                ('Display_resolution', models.CharField(max_length=100)),
                ('Display_size', models.CharField(max_length=100)),
                ('Operating_System', models.CharField(max_length=100)),
                ('CPU', models.CharField(max_length=100)),
                ('Chipset', models.CharField(max_length=100)),
                ('GPU', models.CharField(max_length=100)),
                ('Memory_card', models.CharField(max_length=100)),
                ('Internal_memory', models.CharField(max_length=100)),
                ('RAM', models.CharField(max_length=100)),
                ('Primary_camera', models.CharField(max_length=100)),
                ('Secondary_camera', models.CharField(max_length=100)),
                ('Loud_speaker', models.CharField(max_length=100)),
                ('Audio_jack', models.CharField(max_length=100)),
                ('WLAN', models.CharField(max_length=100)),
                ('Bluetooth', models.CharField(max_length=100)),
                ('GPS', models.CharField(max_length=100)),
                ('NFC', models.CharField(max_length=100)),
                ('Radio', models.CharField(max_length=100)),
                ('USB', models.CharField(max_length=100)),
                ('Sensors', models.CharField(max_length=100)),
                ('Battery', models.CharField(max_length=100)),
                ('Colors', models.CharField(max_length=100)),
                ('createdAt', models.CharField(max_length=100)),
                ('updatedAt', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Stolen_markers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('imei', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='stolen_phone', to='imeiApp.imei_numbers')),
                ('owner', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.PROTECT, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='imei_numbers',
            name='IdPhoneModel',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='phone_brand', to='imeiApp.phone_brands'),
        ),
    ]
