import stripe
from typing import Optional
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest

from payments.models import Item


# Create your views here.
def buy(request: WSGIRequest, buy_id: Optional[int] = None):
    if request.method == 'GET':
        itm = Item.objects.get(id=buy_id)
        stripe.api_key = 'sk_test_51LhtEkAYYdoqf3vpqsAfL7ks1Xyd7HsDlSW2eBgIeVjJthWK2xrHy9Pxghy4OwXaBCxIvJLEy6hzD96f5TXtG0KQ00g6kleeAL '
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': itm.name,
                    },
                    'unit_amount': itm.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )

        return redirect(session.url, code=303)

def item(request: WSGIRequest, item_id: Optional[int] = None):
    if request.method == 'GET':
        itm = Item.objects.get(id=item_id)
        return render(request, 'item.html', {'itm_id': item_id, 'itm_name': itm.name, 'itm_description': itm.description, 'itm_price': itm.price/100})