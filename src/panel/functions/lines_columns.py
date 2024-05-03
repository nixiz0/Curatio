from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from io import StringIO
from panel.forms import CSVUploadForm
import csv


def del_column(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            columns_to_delete = form.cleaned_data['column'].split(',')  # Split column names by comma
            
            # Reading CSV file
            data = csv_file.read().decode('utf-8').splitlines()
            csv_data = list(csv.reader(data))
            
            # Find the indices of the columns to delete
            header = csv_data[0]
            column_indices = [header.index(column) for column in columns_to_delete if column in header]
            
            # Delete columns
            for row in csv_data:
                for index in sorted(column_indices, reverse=True):
                    del row[index]
            
            # Create a new CSV file
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'
            
            output_csv = StringIO()
            writer = csv.writer(output_csv)
            for row in csv_data:
                writer.writerow(row)
            
            response.write(output_csv.getvalue())
            
            return response
    else:
        form = CSVUploadForm()
    
    return render(request, 'csv_gestion/line_col/del_column.html', {'form': form})


def del_row(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            start_row = form.cleaned_data['start_row']
            end_row = form.cleaned_data['end_row']

            try:
                start_row = int(start_row)
                end_row = int(end_row)

                # Reading CSV file
                data = csv_file.read().decode('utf-8').splitlines()
                csv_data = list(csv.reader(data))

                # Check if the specified rows are valid
                if 0 <= start_row <= end_row < len(csv_data):
                    # Delete rows within the specified interval
                    del csv_data[start_row:end_row + 1]

                    # Create a new CSV file
                    response = HttpResponse(content_type='text/csv')
                    response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'

                    writer = csv.writer(response)
                    for row in csv_data:
                        writer.writerow(row)

                    return response
                else:
                    # Handle invalid row indices
                    return HttpResponse("Invalid row indices provided.")
            except ValueError:
                # Handle conversion to integer error
                return HttpResponse("Invalid row indices provided.")
    else:
        form = CSVUploadForm()

    return render(request, 'csv_gestion/line_col/del_row.html', {'form': form})


def add_column(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            new_column_names = form.cleaned_data['column'].split(',')  # Split column names by comma
            
            # Reading CSV file
            data = csv_file.read().decode('utf-8').splitlines()
            csv_data = list(csv.reader(data))
            
            # Add new columns to the header
            header = csv_data[0]
            header.extend(new_column_names)
            
            # Fill each row with empty values for the new columns
            for row in csv_data[1:]:
                row.extend(['' for _ in range(len(new_column_names))])
            
            # Create a new CSV file
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'
            
            output_csv = StringIO()
            writer = csv.writer(output_csv)
            for row in csv_data:
                writer.writerow(row)
            
            response.write(output_csv.getvalue())
            
            return response
    else:
        form = CSVUploadForm()
    
    return render(request, 'csv_gestion/line_col/add_column.html', {'form': form})


def add_row(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
            start_row = form.cleaned_data['start_row']
            end_row = form.cleaned_data['end_row']
            value_to_add = form.cleaned_data['value']

            try:
                start_row = int(start_row)
                end_row = int(end_row)

                # Reading CSV file
                data = csv_file.read().decode('utf-8').splitlines()
                csv_data = list(csv.reader(data))

                # Check if the specified rows and column are valid
                if (
                    0 <= start_row <= end_row < len(csv_data) and
                    column_name in csv_data[0]
                ):
                    column_index = csv_data[0].index(column_name)

                    # Add the value to the specified rows in the column
                    for row in csv_data[start_row:end_row + 1]:
                        row[column_index] = value_to_add

                    # Create a new CSV file
                    response = HttpResponse(content_type='text/csv')
                    response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'

                    writer = csv.writer(response)
                    for row in csv_data:
                        writer.writerow(row)

                    return response
                else:
                    # Handle invalid row indices or column name
                    return HttpResponse("Invalid row indices or column name provided.")
            except ValueError:
                # Handle conversion to integer error
                return HttpResponse("Invalid row indices provided.")
    else:
        form = CSVUploadForm()

    return render(request, 'csv_gestion/line_col/add_row.html', {'form': form})


def modify_column(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            old_column_name = form.cleaned_data['column']
            new_column_name = form.cleaned_data['new_column_name']
            
            # Reading CSV file
            data = csv_file.read().decode('utf-8').splitlines()
            csv_data = list(csv.reader(data))
            
            # Check if the old column name exists in the header
            header = csv_data[0]
            if old_column_name in header:
                # Find the index of the old column name
                column_index = header.index(old_column_name)
                
                # Replace the old column name with the new one
                header[column_index] = new_column_name
                
                # Create a new CSV file
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'
                
                writer = csv.writer(response)
                for row in csv_data:
                    writer.writerow(row)
                
                return response
            else:
                # Handle case where the old column name does not exist
                return HttpResponse("Old column name does not exist in the CSV file.")
    else:
        form = CSVUploadForm()
    
    return render(request, 'csv_gestion/line_col/modify_column.html', {'form': form})


def modify_row(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
            start_row = form.cleaned_data['start_row']
            end_row = form.cleaned_data['end_row']
            new_value = form.cleaned_data['value']

            try:
                start_row = int(start_row)
                end_row = int(end_row)

                # Reading CSV file
                data = csv_file.read().decode('utf-8').splitlines()
                csv_data = list(csv.reader(data))

                # Check if the specified rows and column are valid
                if (
                    0 <= start_row <= end_row < len(csv_data) and
                    column_name in csv_data[0]
                ):
                    column_index = csv_data[0].index(column_name)

                    # Update the specified rows in the column with the new value
                    for i in range(start_row, end_row + 1):
                        csv_data[i][column_index] = new_value

                    # Create a new CSV file
                    response = HttpResponse(content_type='text/csv')
                    response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'

                    writer = csv.writer(response)
                    for row in csv_data:
                        writer.writerow(row)

                    return response
                else:
                    # Handle invalid row indices or column name
                    return HttpResponse("Invalid row indices or column name provided.")
            except ValueError:
                # Handle conversion to integer error
                return HttpResponse("Invalid row indices provided.")
    else:
        form = CSVUploadForm()

    return render(request, 'csv_gestion/line_col/modify_row.html', {'form': form})


def interval(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            column_name = form.cleaned_data['column']
            start_row = form.cleaned_data['start_row']
            end_row = form.cleaned_data['end_row']

            try:
                start_row = int(start_row)

                # Reading CSV file
                data = csv_file.read().decode('utf-8').splitlines()
                csv_data = list(csv.reader(data))

                # Check if the specified column exists
                if column_name not in csv_data[0]:
                    return HttpResponse("Column not found in the CSV file.")

                column_index = csv_data[0].index(column_name)

                # Process the specified interval for each row
                for i in range(1, len(csv_data)):
                    column_data = csv_data[i][column_index]
                    if start_row >= len(column_data):
                        csv_data[i][column_index] = ""
                    else:
                        if end_row == "":
                            csv_data[i][column_index] = column_data[start_row:]
                        else:
                            end_row = int(end_row)
                            if end_row >= len(column_data):
                                end_row = len(column_data) - 1
                            csv_data[i][column_index] = column_data[start_row:end_row + 1]

                # Create a new CSV file
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="{csv_file.name}"'

                writer = csv.writer(response)
                writer.writerows(csv_data)

                return response
            except ValueError:
                # Handle conversion to integer error
                return HttpResponse("Invalid input values.")
    else:
        form = CSVUploadForm()

    return render(request, 'csv_gestion/line_col/interval.html', {'form': form})