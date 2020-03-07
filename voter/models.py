from django.db import models

# Create your models here.

class VoterDetails(models.Model):
    voter_no = models.AutoField(primary_key=True)
    assembly_no = models.TextField()
    part_no = models.IntegerField()
    serial_no = models.IntegerField()
    house_no_eng= models.TextField()
    house_no_hin = models.TextField()
    voter_name_eng = models.TextField()
    voter_name_hin = models.TextField()
    MALE = "male"
    FEMALE = "female"
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    gender = models.CharField(
        max_length=20,
        choices=GENDER,
        default=False,
    )
    relative_name_eng = models.TextField()
    relative_name_hin = models.TextField()
    FATHER = "father"
    MOTHER = "mother"
    HUSBAND = "husband"
    RELATION = [
        (FATHER, 'Father'),
        (MOTHER, 'Mother'),
        (HUSBAND, 'Husband')
    ]
    relation_type = models.CharField(
        max_length=20,
        choices=RELATION,
        default=False,
    )
    age = models.IntegerField()
    voter_id_card_no = models.TextField()
    contact_no = models.IntegerField()
    support_no = models.IntegerField()
    section_eng= models.TextField()
    section_hin = models.TextField()
    booth_eng = models.TextField()
    booth_hin = models.TextField()
    dead = models.BooleanField(default=False)


class Election(models.Model):
    election_id = models.AutoField(primary_key=True)
    election_name = models.TextField()


class Assembly(models.Model):
    assembly_id = models.AutoField(primary_key=True)
    election_id = models.ForeignKey(Election, on_delete=models.CASCADE)
    assembly_name = models.TextField()
    assembly_no = models.IntegerField()
    booth_part = models.IntegerField()


class CustomerDetails(models.Model):
    customer_no = models.AutoField(primary_key=True)
    customer_name_eng = models.TextField()
    customer_name_hin = models.TextField()
    election_id = models.ForeignKey(Election, on_delete=models.CASCADE)
    assembly_id= models.ForeignKey(Assembly, on_delete=models.CASCADE)
    total_booth_part = models.IntegerField()
    remarks = models.TextField()
    app_name = models.TextField()
    party_name_english = models.TextField()
    party_name_hindi = models.TextField()
    activation_key_mobile = models.TextField()
    activation_key_desktop = models.TextField()
    contact_no = models.IntegerField()
    email_id = models.EmailField()
    username = models.TextField()
    password = models.TextField()
    voting_symbol_eng = models.TextField()
    voting_symbol_hin = models.TextField()
    app_id = models.TextField()
    startup_image = models.ImageField()
    frontscreen_image = models.ImageField()
    icon_image = models.ImageField()
    slip_image = models.ImageField()
    message_starts_with_eng = models.TextField()
    message_starts_with_hin = models.TextField()
    is_winner = models.TextField()
    added_by = models.TextField()
    added_on = models.DateField()
    is_survey = models.BooleanField(default=False)
    is_print= models.BooleanField(default=False)


class AppDownload(models.Model):
    app_download_id = models.AutoField(primary_key=True)
    app_id = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    device_id = models.TextField()
    device_type = models.TextField()
    userName = models.TextField()
    email = models.TextField()
    contact_no = models.TextField()
    allowed_list = models.TextField()
    added_date_time= models.DateTimeField()
    is_active = models.BooleanField(default=False)
    app_admin = models.BooleanField(default=False)


class ExtendedData(models.Model):
    data_id = models.AutoField(primary_key=True)
    voter_no = models.ForeignKey(VoterDetails, on_delete=models.CASCADE)
    email_id = models.EmailField()
    caste = models.TextField()
    occupation = models.TextField()
    address = models.TextField()
    society = models.TextField()
    flat_no = models.TextField()
    religion = models.TextField()
    complaints = models.TextField()
    region = models.TextField()
    app_download_id = models.ForeignKey(AppDownload, on_delete=models.CASCADE)
    is_called = models.BooleanField(default=False)
    favourite = models.BooleanField(default=False)
    is_voting_us= models.TextField()
    voted = models.BooleanField(default=False)
    is_custom_sms_sent = models.BooleanField(default=False)
    is_custom_whatsapp_sent = models.BooleanField(default=False)
    is_voter_slip_sent = models.BooleanField(default=False)
    is_family_slip_sent = models.BooleanField(default=False)
    is_slip_with_same_name_sent = models.BooleanField(default=False)
    is_voter_slip_printed = models.BooleanField(default=False)
    is_family_slip_printed = models.BooleanField(default=False)











