from django import forms

from .models import Booking


class BookingForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = Booking

        fields = [
            "name",
            "phone",
            "email",
            "event_type",
            "event_date",
            "event_location",
            "package",
            "notes",
        ]

        widgets = {
            "event_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),

            "package": forms.RadioSelect(),
        }