from django.shortcuts import get_object_or_404
from shop.models import Order
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from django.dispatch import receiver


@receiver(valid_ipn_received)
def valid_ipn_signal(sender, **kwargs):
    ipn = sender
    if ipn.payment_status == 'Completed':
        # payment success
        print("payment successful")
        order = Order.objects.create()
        # order = get_object_or_404(Order, id=ipn.invoice)

        # if order.total_cost() == ipn.mc_gross:
        #     # mark the order as paid
        #     order.paid = True
        #     order.save()