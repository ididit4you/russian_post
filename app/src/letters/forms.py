from django import forms

class BarcodeForm(forms.Form):
    barcode = forms.CharField(
        label='Barcode', max_length=50,
        widget=(
            forms.TextInput(
                attrs={
                    'placeholder': 'Barcode',
                    'class': 'form-control form-control'
                }
            )
        ), 
        required=True)