from django.shortcuts import render
from .models import *

# Create your views here.


def dropdown(request):
    prodObj = ProductModel.objects.all()
    itemObj = ItemModel.objects.all()
    return render(request, 'dropdown.html', {'product': prodObj, 'item': itemObj})
