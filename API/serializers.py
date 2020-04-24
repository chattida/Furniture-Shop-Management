from rest_framework import serializers
from Manage.models import Supplier, Stock


class supplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'address',
                  'phone', 'email', 'account_id']
        read_only_fields = ['id']
        extra_kwargs = {
            # 'email': {'validators': []},
            'name': {"error_messages": {"blank": "* กรุณากรอกชื่อบริษัท"}},
            'address': {"error_messages": {"blank": "* กรุณากรอกที่อยู่"}},
            'phone': {"error_messages": {"blank": "* กรุณากรอกเบอร์มือถือ"}},
            'email': {"error_messages": {"blank": "* กรุณากรอกอีเมล", 'invalid': "* กรุณากรอกอีเมลให้ถูกต้อง"}},
        }

    def validate_phone(self, value):
        if len(value) != 10:
            raise serializers.ValidationError(
                "* กรุณากรอกเบอร์มือถือให้ถูกต้อง")
        return value


class stockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'item_id', 'color', 'amount']
