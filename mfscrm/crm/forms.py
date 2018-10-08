from django import forms
from .models import Customer, Service, Product



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_name', 'organization', 'role', 'bldgeroom', 'account_number', 'address', 'city', 'state', 'zipcode', 'email','website')


class ServiceForm(forms.ModelForm):
        class Meta:
            model = Service
            fields = (
            'customer_name', 'service_category', 'description', 'location', 'setup_time', 'cleanup_time', 'service_charge')

class ProductForm(forms.ModelForm):
   class Meta:
       model = Product
       fields = ('customer_name', 'product', 'description', 'quantity', 'pickup_time', 'service_charge' )