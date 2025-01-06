import stripe 
from django.conf import settings 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.webhook.construct_event( payload, sig_header, settings.STRIPE_WEBHOOK_SECRET )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except: 
        stripe.error.SignatureVertificationError as e:
        # Invalid signature
        return HttpResponse(Status=400)
    return HttpResponse(status=200)
