from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Account.models import Account, Owner, Employee

# Create your views here.

@login_required
def index(request):
    context = {}
    user = request.user
    try:
        owner = Owner.objects.get(user_id=user.id)
        context['acc_type'] = 'Owner'
    except:
        employee = Employee.objects.get(user_id=user.id).department
        if employee == 'PO':
            context['acc_type'] = 'Purchasing_Officer'
        elif employee == 'SO':
            context['acc_type'] = 'Sale_Officer'

    return render(request, template_name='Main/index.html', context=context)
