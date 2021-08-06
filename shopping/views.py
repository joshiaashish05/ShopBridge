from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProductForm
from .models import Product
from django.contrib.auth.models import User
# Create your views here.


def Index(request):
    pro=Product.objects.all()
    return render(request, 'shopping/index.html',{'product': pro })

def allProduct(request):
    pro=Product.objects.all()
    return render(request,'shopping/allproduct.html',{'product': pro })

def addProduct(request):
    if request.method == 'GET':
        return render(request, 'shopping/addproduct.html', {'form': ProductForm()})
    else:
        try:
            form = ProductForm(request.POST)
            addproduct = form.save(commit=False)
            addproduct.user = request.user
            addproduct.save()
            return redirect('shopping:allproduct')
        except ValueError:
            return render(request, 'shopping/addproduct.html', {'form': ProductForm(), 'error': 'ERROR'})
    
def editProduct(request, product_pk):
    pro = get_object_or_404(Product, pk=product_pk)
    if request.method == 'GET':
        form = ProductForm(instance=pro)
        return render(request, 'shopping/editproduct.html', {'product': pro, 'form': form})
    else:
        try:
            form = ProductForm(request.POST, instance=pro)
            form.save()
            return redirect('shopping:allproduct')
        except ValueError:
            return render(request, 'shopping/editproduct.html', {'product': pro, 'form': form, 'error': 'bad info'})

def deleteProduct(request, product_pk):
    pro = get_object_or_404(Product, pk=product_pk)
    if request.method == 'POST':
        pro.delete()
        return redirect('shopping:allproduct')