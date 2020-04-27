import json
from builtins import object

from django.db.models import Q
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Account.models import Employee
from API.serializers import (customerSerializer, employeeSerializer,
                             itemSerializer, stockSerializer,
                             supplierSerializer, userSerializer,
                             accountSerializer)
from Manage.models import Customer, Item, Stock, Supplier, Account
from django.contrib.auth.models import User


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

        if id:
            items = Supplier.objects.filter(pk=id)
        elif sort:
            if (sort == "asc"):
                items = Supplier.objects.filter(Q(name__icontains=search_data) | Q(
                    address__icontains=search_data) | Q(phone__icontains=search_data) | Q(email__icontains=search_data)).order_by(data)
            elif (sort == "desc"):
                items = Supplier.objects.filter(Q(name__icontains=search_data) | Q(
                    address__icontains=search_data) | Q(phone__icontains=search_data) | Q(email__icontains=search_data)).order_by('-' + data)
        elif search:
            items = Supplier.objects.filter(Q(name__icontains=search) | Q(
                address__icontains=search) | Q(phone__icontains=search) | Q(email__icontains=search))
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
        # get parameter search
        try:
            search = request.query_params['search']
            if not search:
                search = " "
            # get parameter del_list
            try:
                del_list = request.query_params['del_list']
                del_list = del_list.split(",")
                del_list = list(map(int, del_list))
            except:
                del_list = []
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
            # get parameter del_list
            try:
                del_list = request.query_params['del_list']
                del_list = del_list.split(",")
                del_list = list(map(int, del_list))
            except:
                del_list = []
        except:
            sort = False

        # get parameter order
        try:
            get_data = request.query_params['get_data']
        except:
            get_data = False

        if get_data:
            items = Stock.objects.filter(id=get_data)
        elif id:
            items = Stock.objects.filter(pk=id)
        elif sort:
            if (sort == "asc"):
                items = Stock.objects.filter(Q(color__icontains=search_data) | Q(amount__icontains=search_data) | Q(item_id__name__icontains=search_data) |
                                             Q(item_id__description__icontains=search_data) | Q(item_id__item_type__icontains=search_data) | Q(item_id__sale_price__icontains=search_data)).exclude(id__in=del_list).order_by(data)
            elif (sort == "desc"):
                items = Stock.objects.filter(Q(color__icontains=search_data) | Q(amount__icontains=search_data) | Q(item_id__name__icontains=search_data) |
                                             Q(item_id__description__icontains=search_data) | Q(item_id__item_type__icontains=search_data) | Q(item_id__sale_price__icontains=search_data)).exclude(id__in=del_list).order_by('-' + data)
        elif search:
            items = Stock.objects.filter(Q(color__icontains=search) | Q(amount__icontains=search) | Q(item_id__name__icontains=search) |
                                         Q(item_id__description__icontains=search) | Q(item_id__item_type__icontains=search) | Q(item_id__sale_price__icontains=search)).exclude(id__in=del_list)
        else:
            items = Stock.objects.all()
        serializer = stockSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        data = json.loads(request.body)
        item_id = Item.objects.get(pk=data.get('item_id'))
        instance = Stock.objects.get(pk=data.get('id'))
        serializer = stockSerializer(
            data=data, instance=instance, partial=True)
        if serializer.is_valid():
            serializer.save(item_id=item_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = json.loads(request.body)
        stock = Stock.objects.get(pk=data.get('id'))
        stock.delete()
        return Response(status=status.HTTP_200_OK)


class api_employee(APIView):
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

        if id:
            items = Employee.objects.filter(pk=id)
        elif sort:
            if (sort == "asc"):
                items = Employee.objects.filter(Q(account__user__first_name__icontains=search_data) |
                                                Q(account__user__last_name__icontains=search_data) | Q(account__user__email__icontains=search_data) |
                                                Q(account__phone__icontains=search_data) | Q(department__icontains=search_data)).order_by(data)
            elif (sort == "desc"):
                items = Employee.objects.filter(Q(account__user__first_name__icontains=search_data) |
                                                Q(account__user__last_name__icontains=search_data) | Q(account__user__email__icontains=search_data) |
                                                Q(account__phone__icontains=search_data) | Q(department__icontains=search_data)).order_by('-' + data)
        elif search:
            items = Employee.objects.filter(Q(account__user__first_name__icontains=search) |
                                            Q(account__user__last_name__icontains=search) | Q(account__user__email__icontains=search) |
                                            Q(account__phone__icontains=search) | Q(department__icontains=search))
        else:
            items = Employee.objects.all()
        serializer = employeeSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        data = json.loads(request.body)
        instance = Employee.objects.get(pk=data.get('id'))
        serializer = employeeSerializer(
            data=data, instance=instance, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = json.loads(request.body)
        employee = Employee.objects.get(pk=data.get('id'))
        employee.delete()
        return Response(status=status.HTTP_200_OK)


class api_customer(APIView):
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

        # get parameter order
        try:
            get_data = request.query_params['get_data']
        except:
            get_data = False

        if get_data:
            items = Customer.objects.filter(id=get_data)
        elif id:
            items = Customer.objects.filter(pk=id)
        elif sort:
            if (sort == "asc"):
                items = Customer.objects.filter(Q(fname__icontains=search_data) | Q(lname__icontains=search_data) | Q(email__icontains=search_data) |
                                                Q(phone__icontains=search_data) | Q(address__icontains=search_data)).order_by(data)
            elif (sort == "desc"):
                items = Customer.objects.filter(Q(fname__icontains=search_data) | Q(lname__icontains=search_data) | Q(email__icontains=search_data) |
                                                Q(phone__icontains=search_data) | Q(address__icontains=search_data)).order_by('-' + data)
        elif search:
            items = Customer.objects.filter(Q(fname__icontains=search) | Q(lname__icontains=search) | Q(email__icontains=search) |
                                            Q(phone__icontains=search) | Q(address__icontains=search))
        else:
            items = Customer.objects.all()
        serializer = customerSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        data = json.loads(request.body)
        instance = Customer.objects.get(pk=data.get('id'))
        serializer = customerSerializer(
            data=data, instance=instance, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = json.loads(request.body)
        customer = Customer.objects.get(pk=data.get('id'))
        customer.delete()
        return Response(status=status.HTTP_200_OK)


class api_item(APIView):
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

        if id:
            items = Item.objects.filter(pk=id)
        elif sort:
            if (sort == "asc"):
                items = Item.objects.filter(Q(name__icontains=search_data) | Q(description__icontains=search_data) | Q(item_type__icontains=search_data) |
                                            Q(purchase_price__icontains=search_data) | Q(sale_price__icontains=search_data) | Q(supplier_id__name__icontains=search_data)).order_by(data)
            elif (sort == "desc"):
                items = Item.objects.filter(Q(name__icontains=search_data) | Q(description__icontains=search_data) | Q(item_type__icontains=search_data) |
                                            Q(purchase_price__icontains=search_data) | Q(sale_price__icontains=search_data) | Q(supplier_id__name__icontains=search_data)).order_by('-' + data)
        elif search:
            items = Item.objects.filter(Q(name__icontains=search) | Q(description__icontains=search) | Q(item_type__icontains=search) |
                                        Q(purchase_price__icontains=search) | Q(sale_price__icontains=search) | Q(supplier_id__name__icontains=search))
        else:
            items = Item.objects.all()
        serializer = itemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        data = json.loads(request.body)
        supplier_id = Supplier.objects.get(pk=data.get('supplier_id'))
        instance = Item.objects.get(pk=data.get('id'))
        serializer = itemSerializer(
            data=data, instance=instance, partial=True)
        if serializer.is_valid():
            serializer.save(supplier_id=supplier_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        data = json.loads(request.body)
        item = Item.objects.get(pk=data.get('id'))
        item.delete()
        return Response(status=status.HTTP_200_OK)


class api_user(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # get parameter id
        try:
            id = request.query_params['id']
        except:
            id = False

        if id:
            items = User.objects.filter(pk=id)
        else:
            items = User.objects.all()
        serializer = userSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        data = json.loads(request.body)
        instance = User.objects.get(pk=data.get('id'))
        serializer = userSerializer(
            data=data, instance=instance, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class api_account(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # get parameter id
        try:
            id = request.query_params['id']
        except:
            id = False

        if id:
            items = Account.objects.filter(pk=id)
        else:
            items = Account.objects.all()
        serializer = accountSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        data = json.loads(request.body)
        instance = Account.objects.get(pk=data.get('id'))
        serializer = accountSerializer(
            data=data, instance=instance, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
