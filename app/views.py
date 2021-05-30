from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    form = CustomerForm()
    if request.method == 'POST':
	    form = CustomerForm(request.POST)
	    if form.is_valid():
		    form.save()
    context={'form':form}
    return render(request,'index.html',context)
