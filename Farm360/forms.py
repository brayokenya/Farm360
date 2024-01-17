# forms.py

from django import forms
from .models import Event, Transaction

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("title", "start_date", "end_date", "description")




class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

        widgets = {
                'attachment': forms.FileInput(attrs={'class': 'custom-file-input'}),
            }
