from django.forms import ModelForm
from django import forms
from .models import Shotinfo
from django.forms import widgets

class ShotinfoForm(ModelForm):
    
    class Meta:
        model = Shotinfo
        
        fields = ['shot_type', 'shot_status', 'shot_record']

        labels = {
            'shot_type':'Type', 
            'shot_status':'Make', 
            'shot_record':'Model', 
       }
