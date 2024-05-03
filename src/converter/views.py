import csv
from io import StringIO
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

from panel.forms import CSVUploadForm


# Create your views here.
def converter(request):
    return render(request, "converter.html")

def string_converter(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
            
            df = pd.read_csv(csv_file)
            
            # Converter the specified column in string
            df[column_name] = df[column_name].astype(str)
            
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'
            df.to_csv(response, index=False)
            
            return response
    else:
        form = CSVUploadForm()
    return render(request, 'csv_converter/str_converter.html', {'form': form})

def object_converter(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
            
            df = pd.read_csv(csv_file)
            
            # Converter the specified column in string
            df[column_name] = df[column_name].astype(object)
            
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'
            df.to_csv(response, index=False)
            
            return response
    else:
        form = CSVUploadForm()
    return render(request, 'csv_converter/object_converter.html', {'form': form})

def int_converter(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
            
            df = pd.read_csv(csv_file)
            
            # Converter the specified column in string
            df[column_name] = pd.to_numeric(df[column_name], errors='coerce', downcast='integer')
            
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'
            df.to_csv(response, index=False)
            
            return response
    else:
        form = CSVUploadForm()
    return render(request, 'csv_converter/int_converter.html', {'form': form})

def float_converter(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
            
            df = pd.read_csv(csv_file)
            
            # Converter the specified column in string
            df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
            
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'
            df.to_csv(response, index=False)
            
            return response
    else:
        form = CSVUploadForm()
    return render(request, 'csv_converter/float_converter.html', {'form': form})

def bool_converter(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
            
            df = pd.read_csv(csv_file)
            
            # Converter the specified column in string
            df[column_name] = df[column_name].astype(bool)
            
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'
            df.to_csv(response, index=False)
            
            return response
    else:
        form = CSVUploadForm()
    return render(request, 'csv_converter/bool_converter.html', {'form': form})

def date_converter(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
            
            df = pd.read_csv(csv_file)
            
            # Converter the specified column in string
            df[column_name] = pd.to_datetime(df[column_name], errors='coerce')
            
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'
            df.to_csv(response, index=False)
            
            return response
    else:
        form = CSVUploadForm()
    return render(request, 'csv_converter/date_converter.html', {'form': form})