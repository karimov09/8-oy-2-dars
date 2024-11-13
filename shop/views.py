from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment
from .forms import CommentForm  

def home(request):
    products = Product.objects.all()  
    return render(request, 'home.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = product.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = CommentForm()

    return render(request, 'product_detail.html', {
        'product': product,
        'comments': comments,
        'form': form,
    })

def product_filter(request):
    product_type = request.GET.get('type')
    products = Product.objects.filter(type=product_type) if product_type else Product.objects.all()

    return render(request, 'product_filter.html', {'products': products})
