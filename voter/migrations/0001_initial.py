# Generated by Django 3.0.4 on 2020-03-07 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppDownload',
            fields=[
                ('app_download_id', models.AutoField(primary_key=True, serialize=False)),
                ('device_id', models.TextField()),
                ('device_type', models.TextField()),
                ('userName', models.TextField()),
                ('email', models.TextField()),
                ('contact_no', models.TextField()),
                ('allowed_list', models.TextField()),
                ('added_date_time', models.DateTimeField()),
                ('is_active', models.BooleanField(default=False)),
                ('app_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('assembly_id', models.AutoField(primary_key=True, serialize=False)),
                ('assembly_name', models.TextField()),
                ('assembly_no', models.IntegerField()),
                ('booth_part', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('election_id', models.AutoField(primary_key=True, serialize=False)),
                ('election_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VoterDetails',
            fields=[
                ('voter_no', models.AutoField(primary_key=True, serialize=False)),
                ('assembly_no', models.TextField()),
                ('part_no', models.IntegerField()),
                ('serial_no', models.IntegerField()),
                ('house_no_eng', models.TextField()),
                ('house_no_hin', models.TextField()),
                ('voter_name_eng', models.TextField()),
                ('voter_name_hin', models.TextField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default=False, max_length=20)),
                ('relative_name_eng', models.TextField()),
                ('relative_name_hin', models.TextField()),
                ('relation_type', models.CharField(choices=[('father', 'Father'), ('mother', 'Mother'), ('husband', 'Husband')], default=False, max_length=20)),
                ('age', models.IntegerField()),
                ('voter_id_card_no', models.TextField()),
                ('contact_no', models.IntegerField()),
                ('support_no', models.IntegerField()),
                ('section_eng', models.TextField()),
                ('section_hin', models.TextField()),
                ('booth_eng', models.TextField()),
                ('booth_hin', models.TextField()),
                ('dead', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ExtendedData',
            fields=[
                ('data_id', models.AutoField(primary_key=True, serialize=False)),
                ('email_id', models.EmailField(max_length=254)),
                ('caste', models.TextField()),
                ('occupation', models.TextField()),
                ('address', models.TextField()),
                ('society', models.TextField()),
                ('flat_no', models.TextField()),
                ('religion', models.TextField()),
                ('complaints', models.TextField()),
                ('region', models.TextField()),
                ('is_called', models.BooleanField(default=False)),
                ('favourite', models.BooleanField(default=False)),
                ('is_voting_us', models.TextField()),
                ('voted', models.BooleanField(default=False)),
                ('is_custom_sms_sent', models.BooleanField(default=False)),
                ('is_custom_whatsapp_sent', models.BooleanField(default=False)),
                ('is_voter_slip_sent', models.BooleanField(default=False)),
                ('is_family_slip_sent', models.BooleanField(default=False)),
                ('is_slip_with_same_name_sent', models.BooleanField(default=False)),
                ('is_voter_slip_printed', models.BooleanField(default=False)),
                ('is_family_slip_printed', models.BooleanField(default=False)),
                ('app_download_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voter.AppDownload')),
                ('voter_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voter.VoterDetails')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('customer_no', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name_eng', models.TextField()),
                ('customer_name_hin', models.TextField()),
                ('total_booth_part', models.IntegerField()),
                ('remarks', models.TextField()),
                ('app_name', models.TextField()),
                ('party_name_english', models.TextField()),
                ('party_name_hindi', models.TextField()),
                ('activation_key_mobile', models.TextField()),
                ('activation_key_desktop', models.TextField()),
                ('contact_no', models.IntegerField()),
                ('email_id', models.EmailField(max_length=254)),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('voting_symbol_eng', models.TextField()),
                ('voting_symbol_hin', models.TextField()),
                ('app_id', models.TextField()),
                ('startup_image', models.ImageField(upload_to='')),
                ('frontscreen_image', models.ImageField(upload_to='')),
                ('icon_image', models.ImageField(upload_to='')),
                ('slip_image', models.ImageField(upload_to='')),
                ('message_starts_with_eng', models.TextField()),
                ('message_starts_with_hin', models.TextField()),
                ('is_winner', models.TextField()),
                ('added_by', models.TextField()),
                ('added_on', models.DateField()),
                ('is_survey', models.BooleanField(default=False)),
                ('is_print', models.BooleanField(default=False)),
                ('assembly_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voter.Assembly')),
                ('election_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voter.Election')),
            ],
        ),
        migrations.AddField(
            model_name='assembly',
            name='election_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voter.Election'),
        ),
        migrations.AddField(
            model_name='appdownload',
            name='app_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voter.CustomerDetails'),
        ),
    ]
