from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import ProtineProduct
from django.conf import settings
import stripe
from django.http import JsonResponse

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        product_data = ProtineProduct.objects.all()
        return ({
            'product':product_data
        })

class Details(View):
    template_name = 'details.html'
    def get(self, request, pk):
        product_data = ProtineProduct.objects.get(pk = pk)
        return render (request, self.template_name,{
            'product':product_data,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })

class CheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        print(request.POST['id'])
        pk = request.POST['id']
        product= ProtineProduct.objects.get(pk = pk)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'inr',
                        'unit_amount': product.product_price * 100,
                        'product_data': {
                            'name': product.product_name,
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": product.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url, code=303)
        # return JsonResponse( {'id':checkout_session.id})