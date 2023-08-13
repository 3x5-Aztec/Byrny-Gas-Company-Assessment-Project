from django.core import validators
from django import forms
from .models import ServiceDatabase

class ServiceRequest(forms.ModelForm):
    class Meta:
        model = ServiceDatabase
        fields = ['customer_name',
                    'request_type',
                    'request_details',
                    'attachment',
                    'status',
                    'submitted_at',
                    'resolved_at']