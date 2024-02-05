import io
from datetime import datetime

import qrcode
from django import forms
from django.template.response import TemplateResponse
from django.urls import path
from django.urls import reverse_lazy
from django.views.generic import FormView
from fatoora import Fatoora
from qrcode.image.svg import SvgPathImage


def string_to_hex(string):
    return string.encode().hex()


class ZatcaQrCodeForm(forms.Form):
    seller_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    tax_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    invoice_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    total_amount = forms.DecimalField(max_digits=12, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    tax_amount = forms.DecimalField(max_digits=12, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))


class ZatcaQrCodeView(FormView):
    template_name = 'zatca_qr_code.html'
    result_template_name = 'zatca_qr_result.html'
    form_class = ZatcaQrCodeForm
    success_url = reverse_lazy("index")
    initial = {
        "seller_name": "Bobs Records",
        "tax_number": "310122393500003",
        "invoice_date": "2022-04-25T15:30:00Z",
        "total_amount": "1200.00",
        "tax_amount": "150.00"
    }

    def form_valid(self, form):
        fatoora_obj = Fatoora(
            seller_name=form.cleaned_data['seller_name'],
            tax_number=form.cleaned_data['tax_number'],
            invoice_date=datetime.timestamp(form.cleaned_data['invoice_date']),
            total_amount=form.cleaned_data['total_amount'],
            tax_amount=form.cleaned_data['tax_amount']
        )
        stream = io.BytesIO()
        img = qrcode.make(fatoora_obj.base64, image_factory=SvgPathImage)
        img.save(stream)
        return TemplateResponse(self.request, self.result_template_name, {'img': stream.getvalue().decode()})


urlpatterns = [
    path('zatca/', ZatcaQrCodeView.as_view(), name='index')
]
