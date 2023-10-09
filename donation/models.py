from django.db import models
from django.shortcuts import reverse
from core.helpers import LongUniqueId, getUniqueId
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.core.mail import send_mail

# Create your models here.
PAYMENT_GATEWAYS = (
    ('paystack', 'Paystack'),
    ('payant', 'Payant'),
    ('paypal', 'Paypal'),
)
class Donation(models.Model):
    uid = models.CharField(default=getUniqueId, max_length=20, editable=False, help_text='Internal reference ID')
    user = models.ForeignKey('dashboard.UserProfile',
                             on_delete=models.SET_NULL, blank=True, null=True,
                             related_name='donations')
    fullname = models.CharField(max_length=100, blank=True, null=True, help_text="Name of User if not Registed")
    email = models.EmailField(blank=True, null=True, help_text="For Unregister Users")
    gateway = models.CharField(max_length=50, choices=PAYMENT_GATEWAYS, default='paystack')
    reference = models.CharField(max_length=255, help_text="Reference from Payment Gateway", blank=True, null=True,)
    transaction_id = models.CharField(max_length=255, help_text="Transaction from Payment Gateway", blank=True, null=True,)
    message = models.CharField(max_length=255, help_text="Message from Payment Gateway", blank=True, null=True,)
    status = models.CharField(max_length=255, help_text="Status string from Payment Gateway", blank=True, null=True,)
    amount = models.DecimalField(max_digits=100, decimal_places=2, help_text='Amount Paid in Naira (₦)')
    note = models.TextField(help_text="Message from Donor", blank=True, null=True,)
    paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, help_text="Transaction Date")

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        ordering = ["-timestamp",]

    def __str__(self):
        if self.user:
            return f'{self.user.user.username}'
        elif self.fullname:
            return f'{self.fullname}'
        else:
            return f'{self.uid}'