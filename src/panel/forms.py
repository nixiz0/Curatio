from django.contrib.auth.forms import UserCreationForm
from django import forms

from panel.models import CuratioUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CuratioUser
        fields = ("email", "firstname", "lastname", "country")
        
class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),
    )
    column = forms.CharField(max_length=100, required=False)
    column2 = forms.CharField(max_length=100, required=False)
    start_row = forms.CharField(max_length=100, required=False)
    end_row = forms.CharField(max_length=100, required=False)
    value = forms.CharField(max_length=100, required=False)
    new_column_name = forms.CharField(max_length=100, required=False)