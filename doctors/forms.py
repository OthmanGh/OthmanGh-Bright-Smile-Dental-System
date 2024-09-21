from django import forms
from .models import Doctor, DoctorClinicAffiliation

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['npi','name', 'email', 'phone_number', 'specialties']  
        widgets = {
            'npi': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'specialties': forms.CheckboxSelectMultiple,  
        }
        

class DoctorClinicAffiliationForm(forms.ModelForm):
    class Meta:
        model = DoctorClinicAffiliation
        fields = ['doctor', 'clinic', 'office_address', 'working_days', 'start_time', 'end_time']
        widgets = {
            'office_address': forms.Textarea(attrs={'rows': 3}),
            'working_days': forms.CheckboxSelectMultiple(),
            'start_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'end_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }
    

class AffiliationEditForm(forms.ModelForm):
    class Meta:
        model = DoctorClinicAffiliation
        fields = ['office_address', 'working_days', 'start_time', 'end_time']
        widgets = {
            'office_address': forms.Textarea(attrs={'rows': 3}),
            'working_days': forms.CheckboxSelectMultiple(),
            'start_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'end_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }