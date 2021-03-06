import stripe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission
from django.views.generic.base import TemplateView
from django.conf import settings
from django.shortcuts import render


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class OrdersPageView(LoginRequiredMixin, TemplateView):
    template_name = 'orders/purchase.html'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context



def charge(request):
    # Get permission
    permission = Permission.objects.get(codename='special_status')
    # Get user
    user = request.user
    # Add user permission
    user.user_permissions.add(permission)
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )
        return render(request, 'orders/charge.html')
