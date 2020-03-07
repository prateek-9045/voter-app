from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import VoterDetails, ExtendedData, AppDownload, Assembly, CustomerDetails, Election
from voter.api.serializers import userSerializers, voter_details_Serializers, app_download_Serializers, election_Serializers, assembly_Serializers, customer_details_Serializers, extended_data_Serializers


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class VoterDetailsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        voter = VoterDetails.objects.all()
        serializer = voter_details_Serializers(voter, many=True)
        custom_data = {'status': serializer.data}
        return Response(custom_data)


class ExtendedDataView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = ExtendedData.objects.all()
        serializer = extended_data_Serializers(data, many=True)
        custom_data = {'status': serializer.data}
        return Response(custom_data)


class AppDownloadView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        download = AppDownload.objects.all()
        serializer = app_download_Serializers(download, many=True)
        custom_data = {'status': serializer.data}
        return Response(custom_data)


class AssemblyView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        assembly = Assembly.objects.all()
        serializer = assembly_Serializers(assembly, many=True)
        custom_data = {'status': serializer.data}
        return Response(custom_data)


class ElectionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        election = Election.objects.all()
        serializer = election_Serializers(election, many=True)
        custom_data = {'status': serializer.data}
        return Response(custom_data)


class CustomerDetailsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        cus_detail = CustomerDetails.objects.all()
        serializer = customer_details_Serializers(cus_detail, many=True)
        custom_data = {'status': serializer.data}
        return Response(custom_data)