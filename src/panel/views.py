from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
import pandas as pd

from panel.forms import UserRegistrationForm, CSVUploadForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("panel")
            
    else: 
        form = UserRegistrationForm()
    
    return render(request, "accounts/register.html", {"form": form})

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = UserRegistrationForm(instance=request.user)
    
    return render(request, "user-profile.html", {'form': form, 'user':user})

def panel(request):
    return render(request, "panel.html")


def import_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            
            # Get the file name
            file_name = csv_file.name

            # Read the contents of the CSV file using pandas 
            df = pd.read_csv(csv_file)
            df_head = df.head(51)
            
            df_shape = df.shape
            df_shape0 = df_shape[0]
            df_shape1 = df_shape[1]
            
            # Missing Values Analyze
            df_miss_val = df.isna().sum()
            
            # Transformation Object Types Columns
            object_dtypes = df.select_dtypes(include='object').dtypes

            return render(request, 'panel.html', {'df':df, 'file_name':file_name, 'df_head':df_head, 
                                                  'df_miss_val':df_miss_val, 'object_dtypes':object_dtypes,
                                                   'df_shape':df_shape, 'df_shape0':df_shape0, 'df_shape1':df_shape1})
    else:
        form = CSVUploadForm()
    return render(request, 'csv_gestion/upload.html', {'form': form})