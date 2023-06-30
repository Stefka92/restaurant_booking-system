from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    # Additional form fields and validation can be added here

    def clean_num_guests(self):
        num_guests = self.cleaned_data.get('num_guests')
        if num_guests <= 0:
            raise forms.ValidationError("Number of guests must be greater than zero.")
        return num_guests

    class Meta:
        model = Reservation