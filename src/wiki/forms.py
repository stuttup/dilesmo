from django import forms

from .models import Queries

class QueriesForm(forms.ModelForm):

    class Meta:
        model = Queries
        fields = ('query',)