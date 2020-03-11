from django.shortcuts import render
from rest_framework import status
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import VoterDetails, ExtendedData, AppDownload, Assembly, CustomerDetails, Election
from voter.api.serializers import userSerializers, voter_details_Serializers, app_download_Serializers, election_Serializers, assembly_Serializers, customer_details_Serializers, extended_data_Serializers
from django.conf.urls import url
from django.urls import path


class HelloView(APIView):

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class VoterDetailsView(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        voter = VoterDetails.objects.all()
        serializer = voter_details_Serializers(voter, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = voter_details_Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def put(self, request, pk):
        voter_data = VoterDetails.objects.get(pk = pk)
        serializer = voter_details_Serializers(voter_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class ExtendedDataView(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = ExtendedData.objects.all()
        serializer = extended_data_Serializers(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = extended_data_Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        
    def put(self, request, pk):
        ext_data = ExtendedData.objects.get(pk = pk)
        serializer = extended_data_Serializers(ext_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      


class AppDownloadView(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        download = AppDownload.objects.all()
        serializer = app_download_Serializers(download, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = app_download_Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

    def put(self, request, pk):
        app_data = AppDownload.objects.get(pk = pk)
        serializer = app_download_Serializers(app_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     


class AssemblyView(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        assembly = Assembly.objects.all()
        serializer = assembly_Serializers(assembly, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = assembly_Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def put(self, request, pk):
        assembly_data = Assembly.objects.get(pk = pk)
        serializer = assembly_Serializers(assembly_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class ElectionView(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        election = Election.objects.all()
        serializer = election_Serializers(election, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = election_Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def put(self, request, pk):
        election_data = Election.objects.get(pk = pk)
        serializer = election_Serializers(election_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      


class CustomerDetailsView(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request):
        cus_detail = CustomerDetails.objects.all()
        serializer = customer_details_Serializers(cus_detail, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = customer_details_Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

    def put(self, request, pk):
        cus_data = CustomerDetails.objects.get(pk = pk)
        serializer = customer_details_Serializers(cus_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     