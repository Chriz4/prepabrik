from django import forms

from .models import LogBarang

class LogBarangModelForm(forms.ModelForm):

    # barang = forms.ChoiceField(widget=Select)

    class Meta:
        model = LogBarang
        fields = ['barang', 'jumlah']
        
    def __init__(self, *args, **kwargs):
        super(LogBarangModelForm, self).__init__(*args, **kwargs)
        self.fields['barang'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['jumlah'].widget=forms.NumberInput(attrs={
            'class': 'form-control'
        })