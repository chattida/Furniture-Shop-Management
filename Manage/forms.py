from django import forms
from Manage.models import Customer


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
