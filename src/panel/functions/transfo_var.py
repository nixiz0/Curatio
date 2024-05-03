from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
import pandas as pd
import io
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

from panel.forms import CSVUploadForm


def transfo_var_onehot(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
            
            # Reading CSV file
            data = csv_file.read().decode('utf-8')
            
            # Convert CSV data to a DataFrame
            df = pd.read_csv(io.StringIO(data))
            
            # Perform one-hot encoding on the specified column
            encoded_df = pd.get_dummies(df, columns=[column_name], dtype=int)
            
            # Create a new CSV file
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'
            
            # Write the encoded DataFrame to the response
            encoded_df.to_csv(response, index=False)
            
            return response
    else:
        form = CSVUploadForm()
    
    return render(request, 'csv_gestion/transfo_var/transfo_var_onehot.html', {'form': form})


def transfo_var_label(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
            
            # Reading CSV file
            data = csv_file.read().decode('utf-8')
            
            # Convert CSV data to a DataFrame
            df = pd.read_csv(io.StringIO(data))
            
            # Create a LabelEncoder instance
            label_encoder = LabelEncoder()
            
            # Fit the LabelEncoder on the specified column and transform it
            df[column_name] = label_encoder.fit_transform(df[column_name])
            
            # Create a new CSV file
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'
            
            # Write the DataFrame to the response
            df.to_csv(response, index=False)
            
            return response
    else:
        form = CSVUploadForm()
    
    return render(request, 'csv_gestion/transfo_var/transfo_var_label.html', {'form': form})


def merge_columns(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column1_name = form.cleaned_data['column']
            column2_name = form.cleaned_data['column2']
            new_column_name = form.cleaned_data['new_column_name']
            
            # Reading CSV file
            data = csv_file.read().decode('utf-8')
            
            # Convert CSV data to a DataFrame
            df = pd.read_csv(io.StringIO(data))
            
            # Convert int columns to string
            df[column1_name] = df[column1_name].astype(str)
            df[column2_name] = df[column2_name].astype(str)
            
            # Merge the elements of the two chosen columns into a new column with a space in between
            df[new_column_name] = df[column1_name] + ' ' + df[column2_name]
            
            # Create a new CSV file
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'
            
            # Write the DataFrame to the response
            df.to_csv(response, index=False)
            
            return response
    else:
        form = CSVUploadForm()
    
    return render(request, 'csv_gestion/transfo_var/merge_columns.html', {'form': form})


def transfo_var_ordinal(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
            
            # Reading CSV file
            data = csv_file.read().decode('utf-8')
            
            # Convert CSV data to a DataFrame
            df = pd.read_csv(io.StringIO(data))
            
            # Create an OrdinalEncoder instance
            ordinal_encoder = OrdinalEncoder()
            
            # Fit the OrdinalEncoder on the specified column and transform it
            df[column_name] = ordinal_encoder.fit_transform(df[[column_name]])
            
            # Create a new CSV file
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'
            
            # Write the DataFrame to the response
            df.to_csv(response, index=False)
            
            return response
    else:
        form = CSVUploadForm()
    
    return render(request, 'csv_gestion/transfo_var/transfo_var_ordinal.html', {'form': form})