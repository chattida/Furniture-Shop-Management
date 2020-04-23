from django.shortcuts import render
from Manage.forms import addCustomerForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def manage_customer(request):
    return render(request, template_name='Manage/manage_customer.html')


@login_required
def add_customer(request):
    form = addCustomerForm()
    return render(request, template_name='Add/add_customer.html', context={'form': form})
