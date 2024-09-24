from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    """ Task to send e-mail notification when an order is successfully created. """
    try :
        order = Order.objects.get(id=order_id)
        subject = f'Order nr. {order_id}'
        message = ( f'Dear {order.first_name},\n\n' f'You have successfully placed an order.' f'Your order ID is {order_id}.' )
        mail_sent = send_mail( subject, message, 'admin@gmail.com', [order.email] )
        return mail_sent
    except Order.DoesNotExit:
        print(f"Order with ID {order_id} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}") 
    