from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from panel.forms import CSVUploadForm
import csv
import pandas as pd


def order_by(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            sort_column_name = form.cleaned_data['column']

            try:
                # Reading CSV file using pandas
                df = pd.read_csv(csv_file)

                # Check if the specified column exists in the DataFrame
                if sort_column_name not in df.columns:
                    raise KeyError(f"Column '{sort_column_name}' not found in the CSV file.")

                # Sort the DataFrame by the specified column in ascending order
                df.sort_values(by=sort_column_name, ascending=True, inplace=True)

                # Create a new CSV file with the sorted data
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'

                # Write the sorted DataFrame to the response
                df.to_csv(response, index=False)

                return response

            except KeyError as e:
                error_message = str(e)
                form.add_error('column', error_message)
    else:
        form = CSVUploadForm()

    return render(request, 'csv_gestion/line_col/order_by.html', {'form': form})


def reversed_order(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            sort_column_name = form.cleaned_data['column']

            try:
                # Reading CSV file using pandas
                df = pd.read_csv(csv_file)

                # Check if the specified column exists in the DataFrame
                if sort_column_name not in df.columns:
                    raise KeyError(f"Column '{sort_column_name}' not found in the CSV file.")

                # Sort the DataFrame by the specified column in ascending order
                df.sort_values(by=sort_column_name, ascending=False, inplace=True)

                # Create a new CSV file with the sorted data
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'

                # Write the sorted DataFrame to the response
                df.to_csv(response, index=False)

                return response

            except KeyError as e:
                error_message = str(e)
                form.add_error('column', error_message)
    else:
        form = CSVUploadForm()

    return render(request, 'csv_gestion/line_col/reversed_order.html', {'form': form})