from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import product, contact_us, order
import json
from django.core.serializers import serialize
from django.contrib import messages
from collections import namedtuple
from django.contrib.auth.models import User, auth


# Create your views here.
def index(request):
    mydata = product.objects.all()
    context = {
        'members': mydata,
    }
    return render(request, 'shop/home.html', context)


def home(request):
    if request.method == 'POST':
        mydata = product.objects.all()
        context = {
            'members': mydata,
        }
        return render(request, 'shop/index.html', context)
    else:
        return redirect("/")


def aboutus(request):
    return render(request, "shop/aboutus.html")


def contactus(request):
    if request.method == 'POST':
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        uname = request.POST["uname"]
        eaddress = request.POST["eaddress"]
        tarea = request.POST["tarea"]
        contact = contact_us(fname=fname, lname=lname, uname=uname, eaddress=eaddress, tarea=tarea)
        contact.save()
        messages.info(request, "Thank You for contact with us. We will get back you soon!")
        return render(request, "shop/contactus.html")
    else:
        return render(request, "shop/contactus.html")


def cart_f(request):
    if request.method == 'POST':
        cart_items = request.POST.get('cart');
        # print(cart_items)
        # print(type(cart_items))
        x = ""
        try:
            x = json.loads(cart_items)
        except Exception as e:
            print(x)
            print(e)
        cart_list = []
        for y in x:
            cart_list.append(int(y))
        print(cart_list)
        mydata = product.objects.filter(pk__in=cart_list)
        data = serialize("json", mydata, fields=('id', 'price'))
        cart_dict = {}
        for n in mydata:
            cart_dict[str(n.id)] = n.price
        # y = json.dumps(cart_dict)
        # print(type(cart_dict))

        cart_dict = json.dumps(cart_dict)
        print(cart_dict)
        context = {
            'members': mydata,
            'cart_prod': x,
            'cart_json': cart_dict,
        }

        return render(request, "shop/cart.html", context)
    else:
        return redirect("/")


def products(request):
    mydata = product.objects.all().order_by('-pub_date')
    context = {
        'members': mydata,
    }
    return render(request, "shop/product.html", context)


def products_sort(request, sort):
    mydata = product.objects.all().order_by(sort)
    context = {
        'members': mydata,
    }
    return render(request, "shop/product.html", context)


def filters(request, filters):
    mydata = product.objects.filter(category=filters).values()
    # print( "\'" + filters + "\'")
    # print(type(filters))
    # print(mydata)
    context = {
        'members': mydata,
    }
    return render(request, "shop/product_cate.html", context)


def products_cate_sort(request, filters, sort):
    mydata = product.objects.all().filter(category=filters).order_by(sort)
    context = {
        'members': mydata,
    }
    return render(request, "shop/product_cate.html", context)


def product_details(request, de_prod_id):
    mydata = product.objects.all().filter(id=de_prod_id)
    print(mydata)
    context = {
        'members': mydata,
    }
    return render(request, "shop/product_details.html", context)


def checkout(request):
    if request.method == 'POST':
        cart_item = request.POST.get('checkout')
        x = ""
        try:
            x = json.loads(cart_item)
        except Exception as e:
            print(x)
            print(e)
        cart_list = []
        for y in x:
            cart_list.append(int(y))
        print(cart_list)
        mydata = product.objects.filter(pk__in=cart_list)
        cart_dict = {}
        for n in mydata:
            cart_dict[str(n.id)] = x[str(n.id)]
        print(cart_dict)
        total_price = 0
        for k in x:
            for z in mydata:
                if int(k) == z.id:
                    prod_price = z.price
                    count = x[k]
                    total_price = total_price + (count * prod_price)
        print(total_price)
        checkout = True
        context = {
            'members': mydata,
            'cart_count': cart_dict,
            'cart_total_price': total_price,
            'checkout': checkout,
        }
        return render(request, "shop/checkout.html", context)


def order_placed(request):
    if request.method == 'POST':
        cart_value = request.POST.get('cart_value')
        cart_price = request.POST.get('cart_price')
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        pnumber = request.POST["pnumber"]
        address = request.POST["area"] + " " + request.POST["landmark"] + " " + request.POST["city"]
        email = request.POST["email"]
        state = request.POST["state"]
        zip = request.POST["zip"]
        Order = order(order_details=cart_value, total_amount=cart_price, fname=fname, lname=lname, pnumber=pnumber,
                      address=address, email=email, state=state, zip=zip)
        Order.save()
        cart_clear = True
        mydata = order.objects.all().filter(order_details=cart_value, total_amount=cart_price, fname=fname, lname=lname,
                                            pnumber=pnumber, address=address, email=email, state=state, zip=zip)
        for v in mydata:
            id = v.order_id
        return render(request, "shop/checkout.html", {'cart_clear': cart_clear, 'id': id})


def main_menu(request):
    return redirect("/products")
