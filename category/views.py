from django.shortcuts import render, redirect
from .forms import Category_Form
# Create your views here.

def category(request):
    if request.method == 'POST':
        category_form = Category_Form(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
    else:
        category_form = Category_Form()
    return render(request,'category.html',{'form': category_form})
