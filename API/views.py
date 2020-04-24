import json

from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from API.serializers import stockSerializer, supplierSerializer
from Manage.models import Stock, Supplier

# Create your views here.


class api_supplier(APIView):

    def get(self, request):
        #get search
        try:
            search = request.query_params['search']
        except:
            search = False

        #get id
        try:
            id = request.query_params['id']
        except:
            id = False

        if search:
            items = Supplier.objects.filter(Q(name__icontains=search) | Q(
                address__icontains=search) | Q(phone__icontains=search) | Q(email__icontains=search))
        elif id:
            items = Supplier.objects.filter(pk=id)
        else:
            items = Supplier.objects.all()
        serializer = supplierSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        data = json.loads(request.body)
        instance = Supplier.objects.get(pk=data.get('id'))
        serializer = supplierSerializer(
            data=data, instance=instance, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class api_view_stock(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Stock.objects.all()
        serializer = stockSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
