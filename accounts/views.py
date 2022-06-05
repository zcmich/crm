from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from .models import *
from .forms import OrderForm


# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    total_customer = customers.count()
    pending = orders.filter(status='Pending').count()
    delivered = orders.filter(status='Delivered').count()

    context ={'orders':orders, 'customers':customers, 
              'total_orders':total_orders, 'total_customer': total_customer , 'pending':pending, 'delivered':delivered }

    return render(request,'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html', {'products':products}) #"products":"products" "name_to_be_used:"name declared in views.py"

def customer(request, pk_test): #second parameter is name of the variable gooten from url

    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()

    context ={'customer':customer, 'orders':orders, 'order_count':order_count}

    return render(request,'accounts/customers.html',context)

def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})
    if request.method == 'POST' :
        # print('Printing POST', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context= {'form':form}
    return render(request,'accounts/order_form.html',context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST' :
        # print('Printing POST', request.POST)
        form = OrderForm(request.POST, instance=order) #instance=order so it does create new object but rather save on current object
        if form.is_valid():
            form.save() 
            return redirect('/')

    context= {'form':form}
    return render(request,'accounts/order_form.html',context)


def deleteOrder(request, pk):
    order= Order.objects.get(id=pk)
    if request.method == 'POST' :
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request,'accounts/delete.html',context)
