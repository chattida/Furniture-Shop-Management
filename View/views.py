from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def view_supplier(request):
    return render(request, template_name='View/view_supplier.html')
