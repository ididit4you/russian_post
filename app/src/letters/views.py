from django.shortcuts import render
from django.http import HttpResponse

from .forms import BarcodeForm

# Create your views here.
def letter_view(request):
    template = 'letters/letter.html'
    form = BarcodeForm()
    context = {} 
    
    barcode = request.GET.get('barcode')
    
    if barcode:
        form = BarcodeForm(request.GET)

        if form.is_valid():
            context['barcode'] = form.cleaned_data['barcode']
    
    context['form'] = form
        
    return render(request, template, context)