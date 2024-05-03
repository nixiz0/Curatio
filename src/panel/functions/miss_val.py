from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
import pandas as pd

from panel.forms import CSVUploadForm


def miss_val_mean(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
        
            # Read the contents of the CSV file using pandas
            df = pd.read_csv(csv_file)
            
            try:
                # Calculate the mean of the specified column
                mean_value = df[column_name].mean()
                
                # Fill missing values in the specified column with the mean
                df[column_name].fillna(mean_value, inplace=True)
                
                # Create a new CSV file with the filled values
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="filled_{csv_file.name}"'
                
                # Write the DataFrame with filled values to the response
                df.to_csv(response, index=False)
                
                return response
            except KeyError as e:
                error_message = str(e)
                form.add_error('column', error_message)
    else:
        form = CSVUploadForm()
    
    return render(request, 'csv_gestion/miss_val/miss_val_mean.html', {'form': form})


def miss_val_median(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
        
            # Read the contents of the CSV file using pandas
            df = pd.read_csv(csv_file)
            
            try:
                # Calculate the median of the specified column
                mean_value = df[column_name].median()
                
                # Fill missing values in the specified column with the mean
                df[column_name].fillna(mean_value, inplace=True)
                
                # Create a new CSV file with the filled values
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="filled_{csv_file.name}"'
                
                # Write the DataFrame with filled values to the response
                df.to_csv(response, index=False)
                
                return response
            except KeyError as e:
                error_message = str(e)
                form.add_error('column', error_message)
    else:
        form = CSVUploadForm()
    
    return render(request, 'csv_gestion/miss_val/miss_val_median.html', {'form': form})


def miss_val_std(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
        
            # Read the contents of the CSV file using pandas
            df = pd.read_csv(csv_file)
            
            try:
                # Calculate the std of the specified column
                mean_value = df[column_name].std()
                
                # Fill missing values in the specified column with the mean
                df[column_name].fillna(mean_value, inplace=True)
                
                # Create a new CSV file with the filled values
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="filled_{csv_file.name}"'
                
                # Write the DataFrame with filled values to the response
                df.to_csv(response, index=False)
                
                return response
            except KeyError as e:
                error_message = str(e)
                form.add_error('column', error_message)
    else:
        form = CSVUploadForm()
    
    return render(request, 'csv_gestion/miss_val/miss_val_std.html', {'form': form})


def miss_val_del(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
        
            # Read the contents of the CSV file using pandas
            df = pd.read_csv(csv_file)
            
            try:
                # Drop the missing values on the column
                df.dropna(subset=[column_name], inplace=True)
                
                # Create a new CSV file with the filled values
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="filled_{csv_file.name}"'
                
                # Write the DataFrame with filled values to the response
                df.to_csv(response, index=False)
                
                return response
            except KeyError as e:
                error_message = str(e)
                form.add_error('column', error_message)
    else:
        form = CSVUploadForm()
    
    return render(request, 'csv_gestion/miss_val/miss_val_del.html', {'form': form})


def miss_val_define(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
            fill_value = form.cleaned_data['value']

            # Read the contents of the CSV file using pandas
            df = pd.read_csv(csv_file)

            try:
                # Fill missing values in the specified column with the user-defined fill value
                df[column_name].fillna(fill_value, inplace=True)

                # Create a new CSV file with the filled values
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="filled_{csv_file.name}"'

                # Write the DataFrame with filled values to the response
                df.to_csv(response, index=False)

                return response
            except KeyError as e:
                error_message = str(e)
                form.add_error('column', error_message)
    else:
        form = CSVUploadForm()

    return render(request, 'csv_gestion/miss_val/miss_val_define.html', {'form': form})


def miss_val_mode(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
        
            # Read the contents of the CSV file using pandas
            df = pd.read_csv(csv_file)
            
            try:
                # Calculate the mode of the specified column
                mode_value = df[column_name].mode()[0] # Select the first mode if we have more than one
                
                # Fill missing values in the specified column with the mean
                df[column_name].fillna(mode_value, inplace=True)
                
                # Create a new CSV file with the filled values
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="filled_{csv_file.name}"'
                
                # Write the DataFrame with filled values to the response
                df.to_csv(response, index=False)
                
                return response
            except KeyError as e:
                error_message = str(e)
                form.add_error('column', error_message)
    else:
        form = CSVUploadForm()
    
    return render(request, 'csv_gestion/miss_val/miss_val_mode.html', {'form': form})