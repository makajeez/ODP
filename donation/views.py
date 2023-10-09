from django.shortcuts import render
from .models import Donation
from django.views.generic import View
from django.shortcuts import redirect, reverse
from dashboard.models import Address, UserProfile
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from core.helpers_sub import getPaymentKey
from django.contrib import messages
from core.models import HomePageSlider

# Create your views here.


class donationFrameView(View):
    def get(self, *args, **kwargs):
        context = {}
        payment_key = getPaymentKey('paystack-key')
        
        context['payment_key'] = payment_key
        return render(self.request, "donation/donation_ipage.html", context)

class donationView(View):
    def get(self, *args, **kwargs):
        context = {}
        payment_key = getPaymentKey('paystack-key')
        
        context['payment_key'] = payment_key
        return render(self.request, "donation/donation.html", context)

    def post(self, *args, **kwargs):
        context = {
        'amount': self.request.POST.get('amount'),
        'fullname': self.request.POST.get('fullname'),
        'email': self.request.POST.get('email'),
        'phone': self.request.POST.get('phone'),
        'note': self.request.POST.get('note'),
        }
        # url = reverse('donation:payment',  kwargs=context)
        # return HttpResponseRedirect(url)
        payment_key = getPaymentKey('paystack-key')
        context['payment_key'] = payment_key
        return render(self.request, "donation/payment.html", context)
        

class PaymentView(View):
    template_name = "donation/payment.html" #.format(themeVersion())
    def get(self, *args, **kwargs):
        context = {}
        # order = Donation.objects.get(user=self.request.user.profile, paid=False)
        payment_key = getPaymentKey('paystack-key')
        # context['slider'] = HomePageSlider.objects.filter(active=True).first()
        context['payment_key'] = payment_key
        # userprofile = self.request.user.profile
        url = reverse('donation:payment')
        return redirect(url)
        return render(self.request, "donation/payment.html", context)


    def post(self, *args, **kwargs):
        # form = PaymentForm(self.request.POST)
        gateway = self.request.POST.get('gateway')
        fullname = self.request.POST.get('fullname') 
        email = self.request.POST.get('email') 
        status = self.request.POST.get('status') 
        reference = self.request.POST.get('reference')
        transaction = self.request.POST.get('transaction')
        message = self.request.POST.get('message')
        note = self.request.POST.get('note') 
        next_url = self.request.POST.get('next_url')
        amount = self.request.POST.get('amount')
        try:
            # create the payment
            payment = Donation()
            if self.request.user.is_authenticated:
                userprofile = self.request.user.profile #UserProfile.objects.get(user=self.request.user)
                payment.user = userprofile
            else:
                fullname = self.request.POST.get('fullname') 
                payment.fullname = fullname
            payment.email = email
            payment.reference = reference
            payment.transaction_id = transaction
            payment.message = message
            payment.status = status
            payment.amount = amount
            payment.note = note
            payment.save()
            
            messages.success(self.request, "Your Donation was successful!")
            # return redirect("/")
            result = {
                    "message": 'Your Donation was successful, Thank You for your Support',
                    "next_url": '/'
                }
            return JsonResponse(result)
        except Exception as e:
            print('*'*20)
            print(e)
            print('*'*20)
            next_url = '/'
            error = ''' <script>
                        alert("Sorry! There is a technical issue with your Deonation, We have been notified");
                        window.location = "{{NEXT_URL}}";
                        </script> '''.replace("{{NEXT_URL}}", next_url)
            # TODO: send mail on failure
            messages.warning(
                self.request, "A serious error occurred. We have been notifed.")
            return HttpResponse(error)     

        messages.warning(self.request, "Invalid data received")
        return redirect("/")
