from django.shortcuts import render

import stripe
from django.conf import settings

from .models import Product
from django.http import JsonResponse, HttpResponse

stripe.api_key = settings.STRIPE_SECRET_KEY



def home(request):
    product = Product.objects.get(id = 1)
    return render(request, 'home.html', {'product': product, 'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY})



def create_checkout_session(request, id):
    product = Product.objects.get(id = id)
    YOUR_DOMAIN = "http://127.0.0.1:8000/"
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data':{
                    'currency': 'BRL',
                    'unit_amount' : int(product.price),
                    'product_data': {
                        'name': product.name
                    }
                },
                'quantity': 1,
            },
        ],
        payment_method_types=[
            'card',
            'boleto',
        ],
        metadata={
            'id_product': product.id,
        },
        mode='payment',
        success_url=YOUR_DOMAIN + 'sucesso',
        cancel_url=YOUR_DOMAIN + 'erro',
    )
    return JsonResponse({'id': checkout_session.id})


def sucesso(request):
    return HttpResponse('Sucesso!')


def erro(request):
    return HttpResponse('Erro!')




# se fosse em produção
"""

def create_checkout_session(request, id):
    product = Product.objects.get(id = id)
    if settings.DEBUG:
        YOUR_DOMAIN = "http://127.0.0.1:8000/"
    else:
        NOVO_DOMAIN = 'http://seudominio.com.br'

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data':{
                    'currency': 'BRL',
                    'unit_amount' : int(product.price),
                    'product_data': {
                        'name': product.name
                    }
                },
                'quantity': 1,
            },
        ],
        payment_method_types=[
            'card',
            'boleto',
        ],
        metadata={
            'id_product': product.id,
        },
        mode='payment',
        success_url=YOUR_DOMAIN + '/sucesso',
        cancel_url=YOUR_DOMAIN + '/erro',
    )
    return JsonResponse({'id': checkout_session.id})

    
"""