import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView
from .forms import StripeForm


class StripeMixin(object):
    def get_context_data(self):
        context = super(self, StripeMixin().get_context_data(object))
        context['publishable_key'] = settings.STRIPE_PUBLIC_KEY
        return context


class SuccessView(TemplateView):
    template_name = 'product/thank_you.html'


class SubscribeView(StripeMixin, FormView):
    template_name = 'product/subscribe.html'
    form_class = StripeForm
    success_url = HttpResponse('thank_you')

    def form_valid(self, form):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        customer_data = {
            'description': 'Some Customer Data',
            'card': form.cleaned_data['stripe_token']
        }
        customer = stripe.Customer.create(**customer_data)

        customer.subscriptions.create(plan="basic_plan")

        return super(SubscribeView, self).form_valid(form)
