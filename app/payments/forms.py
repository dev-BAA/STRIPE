from django import forms
from django.forms import *

class BuyForm(forms.Form):
    itm_name = CharField(widget=HiddenInput(), required=False)
    itm_description = CharField(widget=HiddenInput(), required=False)
    itm_price = IntegerField(widget=HiddenInput(), required=False)
