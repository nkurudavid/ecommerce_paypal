from django.shortcuts import get_object_or_404
from shop.models import Order
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver


@receiver(valid_ipn_received)
def valid_ipn_signal(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # # payment success
        # print("payment successful")
        order = get_object_or_404(Order, orderCode=ipn.invoice)

        if order:
            # mark the order as paid
            order.is_paid = True
            order.save()