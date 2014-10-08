from django.shortcuts import render


# Create your views here.
def pumpkin(request):
    quantity = int(request.GET.get('quantity', 0))
    price = int(request.GET.get('price', 0))
    spending = quantity * price
    return render(request, "pumpkin/pumpkin.html", {'spending': spending, 'quantity': quantity, 'price': price})