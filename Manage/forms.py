from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from Manage.models import Customer, Supplier, Item
from Account.models import Account, Employee



class addCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('fname', 'lname', 'email', 'phone', 'address')
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control mt-0 mb-2'}),
            'lname': forms.TextInput(attrs={'class': 'form-control mt-0 mb-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-0 mb-2'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mt-0 mb-2'}),
            'address': forms.Textarea(attrs={'class': 'form-control mt-0 mb-2', 'rows': 4})
        }
        labels = {
            'fname': 'ชื่อจริง',
            'lname': 'นามสกุล',
            'email': 'อีเมล์',
            'phone': 'เบอร์มือถือ',
            'address': 'ที่อยู่',
        }
        error_messages = {
            'email': {
                'invalid': ("กรุณากรอกอีเมล์ให้ถูกต้อง"),
                'unique': ("อีเมลล์มีอยู่ในระบบแล้ว")
            }
        }

    def clean_phone(self):
        data = self.cleaned_data.get('phone')
        if len(data) != 10:
            raise ValidationError(
                'กรุณากรอกเบอร์มือถือให้ถูกต้อง',
                code='invalid'
            )
        return data

class addSupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ('name', 'email', 'phone', 'address')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-0 mb-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-0 mb-2'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mt-0 mb-2'}),
            'address': forms.Textarea(attrs={'class': 'form-control mt-0 mb-2', 'rows': 4})
        }
        labels = {
            'name': 'ชื่อบริษัท',
            'email': 'อีเมล์',
            'phone': 'เบอร์มือถือ',
            'address': 'ที่อยู่',
        }
        error_messages = {
            'email': {
                'invalid': ("กรุณากรอกอีเมล์ให้ถูกต้อง"),
                'unique': ("อีเมลล์มีอยู่ในระบบแล้ว")
            }
        }

    def clean_phone(self):
        data = self.cleaned_data.get('phone')
        if len(data) != 10:
            raise ValidationError(
                'กรุณากรอกเบอร์มือถือให้ถูกต้อง',
                code='invalid'
            )
        return data


class addItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'item_type', 'purchase_price', 'sale_price', 'supplier_id')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mt-0 mb-2'}),
            'description': forms.Textarea(attrs={'class': 'form-control mt-0 mb-2', 'rows': 4}),
            'item_type': forms.TextInput(attrs={'class': 'form-control mt-0 mb-2'}),
            'purchase_price': forms.TextInput(attrs={'class': 'form-control mt-0 mb-2'}),
            'sale_price': forms.TextInput(attrs={'class': 'form-control mt-0 mb-2'}),
            'supplier_id': forms.TextInput(attrs={'class': 'form-control mt-0 mb-2'})
        }
        labels = {
            'name': 'ชื่อสินค้า',
            'description': 'รายละเอียดสินค้า',
            'item_type': 'ประเภทสินค้า',
            'purchase_price': 'ราคาซื้อ',
            'sale_price': 'ราคาขาย',
            'supplier_id': 'รหัสผู้ผลิต'
        }
        error_messages = {
            'supplier_id': {
                'invalid_choice': ("ไม่พบข้อมูลผู้ผลิต")
            }
        }