from django import forms
from .models import ContactMessage, QuoteRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "phone", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name", "class": "form-control"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone number", "class": "form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email address", "class": "form-control"}),
            "subject": forms.TextInput(attrs={"placeholder": "Subject", "class": "form-control"}),
            "message": forms.Textarea(attrs={"placeholder": "Tell us about your project...", "class": "form-control", "rows": 6}),
        }

class QuoteForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ["name", "phone", "email", "service", "location", "project_type", "area", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name", "class": "form-control"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone number", "class": "form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email address", "class": "form-control"}),
            "service": forms.Select(attrs={"class": "form-select"}),
            "location": forms.TextInput(attrs={"placeholder": "Project location", "class": "form-control"}),
            "project_type": forms.Select(attrs={"class": "form-select"}),
            "area": forms.TextInput(attrs={"placeholder": "Approx. area, e.g. 1200 sq.ft", "class": "form-control"}),
            "message": forms.Textarea(attrs={"placeholder": "Describe your requirements...", "class": "form-control", "rows": 5}),
        }
