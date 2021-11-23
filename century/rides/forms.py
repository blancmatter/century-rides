from django import forms
from .models import Ride

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = (
            'name', 
            'leader', 
            'location',
            'grade',
            'distance', 
            'speed_mph',
            'date',
            'time',
            'cafe_stop', 
            'drop_ride', 
            'text'
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ride Title'}),
            'leader': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Start Point'}),
            'grade': forms.Select(attrs={'class': 'form-control'}),
            'date': DateInput(),
            'time': TimeInput(),
            'distance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Distance in Miles'}),
            'speed_mph': forms.NumberInput(attrs={'class': 'form-control'}),
            'cafe_stop': forms.CheckboxInput(),
            'drop_ride': forms.CheckboxInput(),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ride Information'}),
        }

class UpdateForm(forms.ModelForm):
    """
    This is a near direct copy of the RideForm, however *if* specifics of the 
    update are only a subset of the original, then it is possible here;
    """
    class Meta:
        model = Ride
        fields = ('name', 'leader', 'distance', 'speed_mph', 'cafe_stop', 'drop_ride', 'text')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ride Title'}),
            'leader': forms.Select(attrs={'class': 'form-control'}),
            'distance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Distance in Miles'}),
            'speed_mph': forms.NumberInput(attrs={'class': 'form-control'}),
            'cafe_stop': forms.CheckboxInput(),
            'drop_ride': forms.CheckboxInput(),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ride Information'}),
        }