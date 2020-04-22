from django.shortcuts import render
from Manage.forms import addCustomerForm

# Create your views here.


def manage_customer(request):
    return render(request, template_name='Manage/manage_customer.html')


def add_customer(request):
    form = addCustomerForm()
    return render(request, template_name='Add/add_customer.html', context={'form': form})
