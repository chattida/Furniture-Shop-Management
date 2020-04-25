import json

from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from API.serializers import stockSerializer, supplierSerializer
from Manage.models import Stock, Supplier, Customer, Stock
from Account.models import Employee

# Create your views here.


class api_supplier(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # get parameter search
        try:
            search = request.query_params['search']
        except:
            search = False

        # get parameter id
        try:
            id = request.query_params['id']
        except:
            id = False

        # get parameter sort
        try:
            sort = request.query_params['sort']
            data = request.query_params['data']
            search_data = request.query_params['search_data']
        except:
            sort = False

        if search:
            items = Supplier.objects.filter(Q(name__icontains=search) | Q(
                address__icontains=search) | Q(phone__icontains=search) | Q(email__icontains=search))
        elif id:
            items = Supplier.objects.filter(pk=id)
        elif sort:
            if (sort == "asc"):
                items = Supplier.objects.filter(Q(name__icontains=search_data) | Q(
                    address__icontains=search_data) | Q(phone__icontains=search_data) | Q(email__icontains=search_data)).order_by(data)
            elif (sort == "desc"):
                items = Supplier.objects.filter(Q(name__icontains=search_data) | Q(
                    address__icontains=search_data) | Q(phone__icontains=search_data) | Q(email__icontains=search_data)).order_by('-' + data)
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

    def delete(self, request):
        data = json.loads(request.body)
        supplier = Supplier.objects.get(pk=data.get('id'))
        supplier.delete()
        return Response(status=status.HTTP_200_OK)


class api_stock(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Stock.objects.all()
        serializer = stockSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        data = json.loads(request.body)
        stock = Stock.objects.get(pk=data.get('id'))
        stock.delete()
        return Response(status=status.HTTP_200_OK)


class api_employee(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        data = json.loads(request.body)
        employee = Employee.objects.get(pk=data.get('id'))
        employee.delete()
        return Response(status=status.HTTP_200_OK)


class api_customer(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        data = json.loads(request.body)
        customer = Customer.objects.get(pk=data.get('id'))
        customer.delete()
        return Response(status=status.HTTP_200_OK)


class api_item(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        data = json.loads(request.body)
        item = Item.objects.get(pk=data.get('id'))
        item.delete()
        return Response(status=status.HTTP_200_OK)
