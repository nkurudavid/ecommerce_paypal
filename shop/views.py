from django.conf import settings
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from decimal import Decimal

from paypal.standard.forms import PayPalPaymentsForm

from .models import Product, Order
# from .forms import CartForm, CheckoutForm

import random



def store(request):
    products = Product.objects.all()
    context =  {
        'products': products,
    }
    return render(request, 'shop/store.html', context)

def process_payment(request, pk):
    product=Product.objects.get(id=pk)
    host = request.get_host()
    order_code=random.randint(0,1000000000)
    Order.objects.create(orderCode=order_code, product=product, amount=product.price).save()


    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': product.price,
        'item_name': product,
        'invoice': 'Order {}'.format(order_code),
        # 'custom': 'a custom value',
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context =  {
        # 'order': order, 
        'form': form,
        'product':product,
    }
    return render(request, 'shop/checkout.html', context)


@csrf_exempt
def payment_done(request):
    messages.success(request, 'You\'ve successfully completed your transaction')
    return redirect(store)


@csrf_exempt
def payment_canceled(request):
    messages.warning(request, 'Your transaction has been canceled.')
    return redirect(store)