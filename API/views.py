from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from API.serializers import supplierSerializer, stockSerializer
from Manage.models import Supplier, Stock

# Create your views here.


class api_view_supplier(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            search = request.query_params['search']
        except:
            search = False
        if search:
            items = Supplier.objects.filter(Q(name__icontains=search) | Q(
                address__icontains=search) | Q(phone__icontains=search) | Q(email__icontains=search))
        else:
            items = Supplier.objects.all()
        serializer = supplierSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class api_view_stock(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Stock.objects.all()
        serializer = stockSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
