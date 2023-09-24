from django.shortcuts import render
from .models import Products,Order  ##because we ae going to use only our products so need to import
from django.core.paginator import Paginator
# Create your views here.
#whatever we need to shows in our website our proucts accoringly we need to create a view model

def front_view(request):
    product_objects = Products.objects.all()
 
## For adding seacrh nav bar    
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

###For adding paginator
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request,'shop_template/front_view.html',{'product_objects':product_objects})
 #now goto app shop and create a template for to use
 #After creation of template we need to link with this urls.py
 

## Adding details of the products
def detail(request,id):
    product_object = Products.objects.get(id=id)
    return render(request, 'shop_template/details.html', {'product_object':product_object})


##checkout 
def checkout(request):
    if request.method== "POST":
        items = request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        address2 = request.POST.get('address2',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order = Order(items=items,name=name,email=email,address=address,address2=address2,city=city,state=state,zipcode=zipcode,total=total)
        order.save()
    return render(request, 'shop_template/checkout.html')
