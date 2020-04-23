from rest_framework import serializers
from Manage.models import Supplier


class supplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'address', 'phone',
                  'email', 'account_id']
