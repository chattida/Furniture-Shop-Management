from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from Manage.models import Customer, Supplier


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
            'name': 'ชื่อ-นามสกุล',
            'email': 'อีเมล์',
            'phone': 'เบอร์มือถือ',
            'address': 'ที่อยู่',
        }