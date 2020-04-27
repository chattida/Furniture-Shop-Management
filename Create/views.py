from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Manage.models import Order, Order_Item, Stock, Item, Customer
from Account.models import Account

# Create your views here.
@login_required
def create_order(request):
    return render(request, template_name='Create/create_order.html')


@login_required
def send_order(request):
    if request.method == 'POST':
        cus_id = request.POST.get('cus-id')
        list_item = request.POST.get('list-item')
        items_value = request.POST.get('items-value')
        total_price = request.POST.get('total-price')

        list_item = list_item.split(",")
        list_item = list(map(int, list_item))
        items_value = items_value.split(",")
        items_value = list(map(int, items_value))
        total_price = float(total_price)

        fail_add = []
        complete_add = []
        total_price_now = 0

        #create order
        orders = Order.objects.create(
            account_id=Account.objects.get(user_id=request.user.id),
            cus_id=Customer.objects.get(id=cus_id),
            total_price=0
        )
        orders.save()

        for i in range(len(list_item)):
            stock = Stock.objects.get(pk=list_item[i])
            amount = stock.amount
            send_amount = items_value[i]

            #Check amount in DB
            if amount < send_amount:
                fail_add.append(send_amount-amount)
                complete_add.append(amount)
                send_amount = amount
            else:
                fail_add.append(0)
                complete_add.append(send_amount)

            # Update Stock
            stock.amount = amount - send_amount
            stock.save()

            # Create order item
            order_items = Order_Item.objects.create(
                    amount=send_amount,
                    color=stock.color,
                    price=stock.item_id.sale_price*send_amount,
                    order_id=orders,
                    item_id=stock.item_id
                )
            order_items.save()

            total_price_now += stock.item_id.sale_price*send_amount

        orders.total_price = total_price_now
        orders.save()

        send_status = {
            'complete_add': complete_add,
            'fail_add': fail_add,
            'total_price': total_price_now,
            'list_item': list_item,
            'items_value': items_value,
            'cus_id': cus_id
        }

        return redirect('index')

    return redirect('index')

@login_required
def show_status(request, id):
    pass