from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings

from goods.models import Info
from .models import Order, OrderLineItem
from bag.contexts import SUBSCRIPTION_COST
from .forms import OrderForm

import stripe
# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'user_trainer_code': request.POST['user_trainer_code'],
        }

        order_form = OrderForm(form_data)
        
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Info.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                        )
                    order_line_item.save()
                except Info.DoesNotExist:
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            print(order_form)
    else:
        bag = request.session.get('bag', {})
        if not bag:
            return redirect(reverse('products'))

        order_form = OrderForm()

    stripe_total = round(SUBSCRIPTION_COST*100)
    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    # Insert Success Message

    if 'bag' in request.session:
        del request.session['bag']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)
