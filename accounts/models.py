from django.db import models
from razao.models import Lancamento
from django import forms

class FormLancamento(forms.ModelForm):
    class Meta:
        model = Lancamento
        exclude = ()
