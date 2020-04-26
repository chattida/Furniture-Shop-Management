from django.shortcuts import render

# Create your views here.
def create_order(request):
    return render(request, template_name='Create/create_order.html')

def send_order(request):
    pass