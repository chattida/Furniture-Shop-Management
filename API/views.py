from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Manage.models import Supplier
from API.serializers import supplierSerializer


# Create your views here.


# @login_required
class api_view_supplier(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Supplier.objects.all()
        serializer = supplierSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
