from rest_framework import serializers
from django.contrib.auth.models import User
from voter.models import VoterDetails, ExtendedData, AppDownload, Assembly, CustomerDetails, Election


class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class voter_details_Serializers(serializers.ModelSerializer):
    class Meta:
        model = VoterDetails
        fields = '__all__'


class extended_data_Serializers(serializers.ModelSerializer):
    class Meta:
        model = ExtendedData
        fields = '__all__'


class app_download_Serializers(serializers.ModelSerializer):
    class Meta:
        model = AppDownload
        fields = '__all__'


class assembly_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Assembly
        fields = '__all__'


class customer_details_Serializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = '__all__'


class election_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = '__all__'