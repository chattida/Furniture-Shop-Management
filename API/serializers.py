from rest_framework import serializers
from Manage.models import Supplier, Stock


class supplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'address',
                  'phone', 'email', 'account_id']
        read_only_fields = ['id']
        # extra_kwargs = {
        #     'email': {'validators': []},
        # }

    def validate_phone(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("phone error")
        return value

    def validate_email(self, value):
        if '@' not in value or '.' not in value:
            raise serializers.ValidationError("email error")
        return value


class stockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'item_id', 'color', 'amount']
