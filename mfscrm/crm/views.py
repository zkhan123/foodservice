from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.utils import timezone


now = timezone.now()


def home(request):
   return render(request, 'crm/home.html',
                 {'crm': home})
@login_required
def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/customer_list.html',
                 {'customers': customer})

@login_required
def customer_edit(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   if request.method == "POST":
       # update
       form = CustomerForm(request.POST, instance=customer)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.updated_date = timezone.now()
           customer.save()
           customer = Customer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/customer_list.html',
                         {'customers': customer})
   else:
        # edit
       form = CustomerForm(instance=customer)
   return render(request, 'crm/customer_edit.html', {'form': form})

@login_required
def customer_delete(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   customer.delete()
   return redirect('crm:customer_list')

@login_required
def service_list(request):
   services = Service.objects.filter(created_date__lte=timezone.now())
   return render(request, 'crm/service_list.html', {'services': services})

@login_required
def product_list(request):
    products = Product.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/products_list.html', {'products': products})

@login_required
def service_new(request):
   if request.method == "POST":
       form = ServiceForm(request.POST)
       if form.is_valid():
           service = form.save(commit=False)
           service.created_date = timezone.now()
           service.save()
           services = Service.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/service_list.html',
                         {'services': services})
   else:
       form = ServiceForm()
       # print("Else")
   return render(request, 'crm/service_new.html', {'form': form})

@login_required
def service_edit(request, pk):
   services = get_object_or_404(Service, pk=pk)
   if request.method == "POST":
       form = ServiceForm(request.POST, instance=services)
       if form.is_valid():
           service = form.save()
           # service.customer = service.id
           service.updated_date = timezone.now()
           service.save()
           service = Service.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/service_list.html', {'service': services})
   else:
       # print("else")
       form = ServiceForm(instance=services)
   return render(request, 'crm/service_edit.html', {'form': form})


@login_required
def service_delete(request, pk):
   service = get_object_or_404(Customer, pk=pk)
   service.delete()
   return redirect('crm:service_list')

@login_required
def products_new(request):
   if request.method == "POST":
       form = ProductForm(request.POST)
       if form.is_valid():
           products = form.save(commit=False)
           products.created_date = timezone.now()
           products.save()
           products = Product.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/products_list.html',
                         {'products': products})
   else:
       form = ServiceForm()
       # print("Else")
   return render(request, 'crm/products_new.html', {'form': form})



# Create your views here.
