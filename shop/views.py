from django.shortcuts import render, redirect
from .models import Product, ProductForm


# Create your views here.
def product_editor(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'index.html', context=context)


def remove_function(request,part_id =None):
    object = Product.objects.get(id=part_id)
    object.delete()
    return redirect('product_editor')

def update_function(request, part_id):

    product = Product.objects.get(id=part_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_editor')
    else:

        form = ProductForm(instance=product)


    return render(request, 'form.html', {'form': form, 'product': product})





