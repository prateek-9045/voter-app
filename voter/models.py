from django.db import models
from django.utils import timezone

# Create your models here.

class VoterDetails(models.Model):
    voter_no = models.AutoField(primary_key=True)
    assembly_no = models.TextField(blank=True)
    part_no = models.IntegerField(blank=True)
    serial_no = models.IntegerField(blank=True)
    house_no_eng= models.TextField(blank=True)
    house_no_hin = models.TextField(blank=True)
    voter_name_eng = models.TextField(blank=True)
    voter_name_hin = models.TextField(blank=True)
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
        blank=True
    )
    relative_name_eng = models.TextField(blank=True)
    relative_name_hin = models.TextField(blank=True)
    FATHER = "father"
    MOTHER = "mother"
    HUSBAND = "husband"
    ORPHAN="orphan"
    RELATION = [
        (FATHER, 'Father'),
        (MOTHER, 'Mother'),
        (HUSBAND, 'Husband'),
    (ORPHAN,"Orphan")
    ]
    relation_type = models.CharField(
        max_length=20,
        choices=RELATION,
        default=False, 
        blank=True
    )
    age = models.IntegerField(blank=True)
    voter_id_card_no = models.TextField(blank=True)
    contact_no = models.TextField(blank=True)
    support_no = models.TextField(blank=True)
    section_eng= models.TextField(blank=True)
    section_hin = models.TextField(blank=True)
    booth_eng = models.TextField(blank=True)
    booth_hin = models.TextField(blank=True)
    dead = models.BooleanField(default=False)
    last_updated_on = models.DateTimeField(default=timezone.now, blank=True, null=True)
    last_updated_by = models.TextField(default=True)

    def __str__(self):
        return self.voter_name_eng


class Election(models.Model):
    election_id = models.AutoField(primary_key=True)
    election_name = models.TextField(blank=True)
    created_on = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_on = models.DateTimeField(default=timezone.now, blank=True, null=True)
    created_by = models.TextField(default=True)
    updated_by = models.TextField(default=True)

    def __str__(self):
        return self.election_name


class Assembly(models.Model):
    assembly_id = models.AutoField(primary_key=True)
    election_id = models.ForeignKey(Election, on_delete=models.CASCADE)
    assembly_name = models.TextField(blank=True)
    assembly_no = models.IntegerField(blank=True)
    booth_part = models.IntegerField(blank=True)
    created_on = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_on = models.DateTimeField(default=timezone.now, blank=True, null=True)
    created_by = models.TextField(default=True)
    updated_by = models.TextField(default=True)

    def __str__(self):
        return self.assembly_name


class CustomerDetails(models.Model):
    customer_no = models.AutoField(primary_key=True)
    customer_name_eng = models.TextField(blank=True)
    customer_name_hin = models.TextField(blank=True)
    election_id = models.ForeignKey(Election, on_delete=models.CASCADE)
    assembly_id= models.ForeignKey(Assembly, on_delete=models.CASCADE)
    total_booth_part = models.IntegerField(blank=True)
    remarks = models.TextField(blank=True)
    app_name = models.TextField(blank=True)
    party_name_english = models.TextField(blank=True)
    party_name_hindi = models.TextField(blank=True)
    activation_key_mobile = models.TextField(blank=True)
    activation_key_desktop = models.TextField(blank=True)
    contact_no = models.IntegerField(blank=True)
    email_id = models.EmailField(blank=True)
    username = models.TextField(blank=True)
    password = models.TextField(blank=True)
    voting_symbol_eng = models.TextField(blank=True)
    voting_symbol_hin = models.TextField(blank=True)
    app_id = models.TextField(blank=True)
    startup_image = models.ImageField(blank=True)
    frontscreen_image = models.ImageField(blank=True)
    icon_image = models.ImageField(blank=True)
    slip_image = models.ImageField(blank=True)
    message_starts_with_eng = models.TextField(blank=True)
    message_starts_with_hin = models.TextField(blank=True)
    is_winner = models.TextField(blank=True)
    is_survey = models.BooleanField(default=False)
    is_print= models.BooleanField(default=False)
    last_updated_on = models.DateTimeField(default=timezone.now, blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now, blank=True, null=True)
    created_by = models.TextField(default=True)
    updated_by = models.TextField(default=True)

    def __str__(self):
        return self.customer_name_eng


class AppDownload(models.Model):
    app_download_id = models.AutoField(primary_key=True)
    app_id = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
    device_id = models.TextField(blank=True)
    device_type = models.TextField(blank=True)
    userName = models.TextField(blank=True)
    email = models.TextField(blank=True)
    contact_no = models.TextField(blank=True)
    allowed_list = models.TextField(blank=True)
    added_date_time= models.DateTimeField(blank=True)
    is_active = models.BooleanField(default=False)
    app_admin = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_on = models.DateTimeField(default=timezone.now, blank=True, null=True)
    created_by = models.TextField(default=True)
    updated_by = models.TextField(default=True)

    def __str__(self):
        return self.app_download_id


class ExtendedData(models.Model):
    data_id = models.AutoField(primary_key=True)
    voter_no = models.ForeignKey(VoterDetails, on_delete=models.CASCADE)
    email_id = models.EmailField(blank=True)
    caste = models.TextField(blank=True)
    occupation = models.TextField(blank=True)
    address = models.TextField(blank=True)
    society = models.TextField(blank=True)
    flat_no = models.TextField(blank=True)
    religion = models.TextField(blank=True)
    complaints = models.TextField(blank=True)
    region = models.TextField(blank=True)
    app_download_id = models.ForeignKey(AppDownload, on_delete=models.CASCADE)
    is_called = models.BooleanField(default=False)
    favourite = models.BooleanField(default=False)
    is_voting_us= models.TextField(blank=True)
    voted = models.BooleanField(default=False)
    is_custom_sms_sent = models.BooleanField(default=False)
    is_custom_whatsapp_sent = models.BooleanField(default=False)
    is_voter_slip_sent = models.BooleanField(default=False)
    is_family_slip_sent = models.BooleanField(default=False)
    is_slip_with_same_name_sent = models.BooleanField(default=False)
    is_voter_slip_printed = models.BooleanField(default=False)
    is_family_slip_printed = models.BooleanField(default=False)
    last_updated_on = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.data_id











