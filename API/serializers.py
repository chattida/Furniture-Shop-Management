from rest_framework import serializers
from Manage.models import Supplier, Stock


class supplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'address', 'phone',
                  'email', 'account_id']


class stockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'item_id', 'color', 'amount']