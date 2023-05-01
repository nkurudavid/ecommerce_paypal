from django.conf import settings
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from decimal import Decimal

from paypal.standard.forms import PayPalPaymentsForm

from .models import Product, Order, OrderItem
# from .forms import CartForm, CheckoutForm

import random



def process_payment(request):
    # order_id = request.session.get('order_id')
    # order = get_object_or_404(Order, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '73.00',
        'item_name': 'Product 1',
        'invoice': 'Order {}'.format(random.randint(0,1000000000)),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context =  {
        # 'order': order, 
        'form': form
    }
    return render(request, 'shop/process_payment.html', context)

    
@csrf_exempt
def payment_done(request):
    messages.success(request, 'You\'ve successfully completed your transaction')
    return redirect(process_payment)


@csrf_exempt
def payment_canceled(request):
    messages.error(request, 'Your transaction has been canceled.')
    return render(process_payment)
