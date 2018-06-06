from django.shortcuts import render_to_response, render
from django.http import HttpResponse
#from django.template import RequestContext
#from sales.models import Sale
from sales.forms import SalePaymentForm
from .models import Product


def home_page(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def product_detail(request, product_id):
    products = Product.objects.get(id=product_id)
    return render(request, 'sales/product_details.html', {'products': products})


def charge(request):
    if request.method == "POST":
        form = SalePaymentForm(request.POST)

        if form.is_valid():  # charges the card
            return HttpResponse("Success! We've charged your card!")
    else:
        form = SalePaymentForm()

    return render(request, "sales/charge.html", {"form": form})

    # return render_to_response("sales/charge.html",
    #                          RequestContext(request, {'form': form}))