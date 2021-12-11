from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order,orderUpdate
from math import ceil
import json
# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values('category')
    print(catprods)
    cats = {item['category'] for item in catprods}
    print(cats)
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        print(prod)
        n= len(prod)
        nslides = ceil(n / 4)
        print(nslides)
        allProds.append([prod,range(1,nslides),nslides])
        print(allProds)

    params = {'allProds':allProds}
    return render(request,'billpay/index.html', params)


def about(request):
    return render(request,'billpay/about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,'billpay/contact.html')
def tracker(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id', '')
        email = request.POST.get('email', '')
        try:
            order =Order.objects.filter(order_id=order_id,email=email)
            if len(order)>0:
                update= orderUpdate.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time':item.timestamp})
                response = json.dumps(updates,default=str)
                print(update)
                print(response)
                print(updates)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request,'billpay/tracker.html')
def search(request):
    return render(request,'billpay/search.html')
def prodview(request, myid):
    #fatch the product using the id
    product = Product.objects.filter(id=myid)
    print("this is id product",product)
    return render(request,'billpay/prodview.html',{'product':product[0]})
def checkout(request):
    if request.method == "POST":
        items_json=request.POST.get('itemsjson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " "+ request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip = request.POST.get('zip', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json,name=name,email=email,address=address,city=city,state=state,zip=zip,phone=phone)
        order.save()
        update = orderUpdate(order_id=order.order_id,update_desc="your oder has been placed")
        update.save()
        thank = True
        id= order.order_id
        return render(request, 'billpay/checkout.html', {'thank':thank , 'id':id})
    return render(request,'billpay/checkout.html')

