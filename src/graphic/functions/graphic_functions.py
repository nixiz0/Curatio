import csv
from zipfile import ZipFile
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO, StringIO
import base64

from panel.forms import CSVUploadForm


def histogram(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            columns = [col.strip() for col in form.cleaned_data['column'].split(',')]

            df = pd.read_csv(csv_file)

            # Build Histograms
            if len(columns) == 1:
                column_name = columns[0]
                plt.figure(figsize=(8, 4)) 
                df[column_name].hist()
                plt.title(f'Histogram of {column_name}')
                plt.tight_layout()

                img_hist = BytesIO()
                plt.savefig(img_hist, format='png')
                plt.close()

                # Create a response with the image
                response = HttpResponse(img_hist.getvalue(), content_type='image/png')
                response['Content-Disposition'] = f'attachment; filename="{column_name}_histogram.png"'

            else:
                img_hist_list = []  # Liste pour stocker les images des histogrammes

                # Build Histograms for multiple columns
                for column_name in columns:
                    plt.figure(figsize=(8, 4)) 
                    df[column_name].hist()
                    plt.title(f'Histogram of {column_name}')
                    plt.tight_layout()

                    img_hist = BytesIO()
                    plt.savefig(img_hist, format='png')
                    plt.close()
                    img_hist_list.append((f'{column_name}_histogram.png', img_hist.getvalue()))

                # Combine all images into a single response as a zip file
                response = HttpResponse(content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename=histograms.zip'

                with ZipFile(response, 'w') as zip_file:
                    for img_name, img_data in img_hist_list:
                        zip_file.writestr(img_name, img_data)

            return response
    else:
        form = CSVUploadForm()
    
    return render(request, 'csv_graphic/graphic_functions/histogram.html', {'form': form})


def boxplot(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            columns = [col.strip() for col in form.cleaned_data['column'].split(',')]

            df = pd.read_csv(csv_file)

            # Build Boxplots
            if len(columns) == 1:
                column_name = columns[0]
                plt.figure(figsize=(8, 4)) 
                df.boxplot(column=column_name)
                plt.title(f'Boxplot of {column_name}')
                plt.tight_layout()

                img_boxplot = BytesIO()
                plt.savefig(img_boxplot, format='png')
                plt.close()

                # Create a response with the image
                response = HttpResponse(img_boxplot.getvalue(), content_type='image/png')
                response['Content-Disposition'] = f'attachment; filename="{column_name}_boxplot.png"'

            else:
                img_boxplot_list = []  # Liste pour stocker les images des boxplots

                # Build Boxplots for multiple columns
                for column_name in columns:
                    plt.figure(figsize=(8, 4)) 
                    df.boxplot(column=column_name)
                    plt.title(f'Boxplot of {column_name}')
                    plt.tight_layout()

                    img_boxplot = BytesIO()
                    plt.savefig(img_boxplot, format='png')
                    plt.close()
                    img_boxplot_list.append((f'{column_name}_boxplot.png', img_boxplot.getvalue()))

                # Combine all images into a single response as a zip file
                response = HttpResponse(content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename=boxplots.zip'

                with ZipFile(response, 'w') as zip_file:
                    for img_name, img_data in img_boxplot_list:
                        zip_file.writestr(img_name, img_data)

            return response
    else:
        form = CSVUploadForm()
    
    return render(request, 'csv_graphic/graphic_functions/boxplot.html', {'form': form})


def scatter(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            columns = [col.strip() for col in form.cleaned_data['column'].split(',')]

            df = pd.read_csv(csv_file)

            # Build Scatter Plot
            if len(columns) == 2:
                x_column, y_column = columns

                plt.figure(figsize=(8, 4))
                plt.scatter(df[x_column], df[y_column])
                plt.title(f'Scatter Plot of {x_column} vs {y_column}')
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.tight_layout()

                img_scatter = BytesIO()
                plt.savefig(img_scatter, format='png')
                plt.close()

                # Create a response with the image
                response = HttpResponse(img_scatter.getvalue(), content_type='image/png')
                response['Content-Disposition'] = f'attachment; filename="{x_column}_vs_{y_column}_scatter.png"'

            else:
                response = HttpResponse("Please provide exactly two column names for a scatter plot.")

            return response
    else:
        form = CSVUploadForm()

    return render(request, 'csv_graphic/graphic_functions/scatter.html', {'form': form})


def pie(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            columns = [col.strip() for col in form.cleaned_data['column'].split(',')]

            df = pd.read_csv(csv_file)

            # Build Pie Charts
            if len(columns) == 1:
                column_name = columns[0]
                plt.figure(figsize=(8, 8))
                counts = df[column_name].value_counts()
                plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
                plt.title(f'Pie Chart of {column_name}')
                plt.tight_layout()

                img_pie = BytesIO()
                plt.savefig(img_pie, format='png')
                plt.close()

                # Create a response with the image
                response = HttpResponse(img_pie.getvalue(), content_type='image/png')
                response['Content-Disposition'] = f'attachment; filename="{column_name}_pie_chart.png"'

            else:
                img_pie_list = []

                # Build Pie Charts for multiple columns
                for column_name in columns:
                    plt.figure(figsize=(8, 8))
                    counts = df[column_name].value_counts()
                    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
                    plt.title(f'Pie Chart of {column_name}')
                    plt.tight_layout()

                    img_pie = BytesIO()
                    plt.savefig(img_pie, format='png')
                    plt.close()
                    img_pie_list.append((f'{column_name}_pie_chart.png', img_pie.getvalue()))

                # Combine all images into a single response as a zip file
                response = HttpResponse(content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename=pie_charts.zip'

                with ZipFile(response, 'w') as zip_file:
                    for img_name, img_data in img_pie_list:
                        zip_file.writestr(img_name, img_data)

            return response
    else:
        form = CSVUploadForm()

    return render(request, 'csv_graphic/graphic_functions/pie.html', {'form': form})


def heatmap(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            columns = [col.strip() for col in form.cleaned_data['column'].split(',')]

            df = pd.read_csv(csv_file)

            # Build Correlation Heatmap
            if len(columns) >= 2:
                plt.figure(figsize=(10, 8))
                correlation_matrix = df[columns].corr()
                sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
                plt.title('Correlation Heatmap')
                plt.tight_layout()

                img_heatmap = BytesIO()
                plt.savefig(img_heatmap, format='png')
                plt.close()

                # Create a response with the image
                response = HttpResponse(img_heatmap.getvalue(), content_type='image/png')
                response['Content-Disposition'] = f'attachment; filename=correlation_heatmap.png'

            else:
                response = HttpResponse("Please provide at least two column names for a correlation heatmap.")

            return response
    else:
        form = CSVUploadForm()

    return render(request, 'csv_graphic/graphic_functions/heatmap.html', {'form': form})


import seaborn as sns

def violin(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            columns = [col.strip() for col in form.cleaned_data['column'].split(',')]

            df = pd.read_csv(csv_file)

            # Build Violin Plot
            if len(columns) >= 1:
                plt.figure(figsize=(10, 8))
                
                if len(columns) == 1:
                    sns.violinplot(x=df[columns[0]], palette='muted')
                else:
                    sns.violinplot(data=df[columns], palette='muted')

                plt.title('Violin Plot')
                plt.tight_layout()

                img_violin = BytesIO()
                plt.savefig(img_violin, format='png')
                plt.close()

                # Create a response with the image
                response = HttpResponse(img_violin.getvalue(), content_type='image/png')
                response['Content-Disposition'] = f'attachment; filename=violin_plot.png'

            else:
                response = HttpResponse("Please provide at least one column name for a violin plot.")

            return response
    else:
        form = CSVUploadForm()

    return render(request, 'csv_graphic/graphic_functions/violin.html', {'form': form})


def butterfly(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            columns = [col.strip() for col in form.cleaned_data['column'].split(',')]

            try:
                df = pd.read_csv(csv_file)
            except pd.errors.EmptyDataError:
                return HttpResponse("The provided CSV file is empty or in an invalid format.")

            # Check if specified columns exist in the DataFrame
            valid_columns = set(df.columns)
            if not set(columns).issubset(valid_columns):
                return HttpResponse("One or more specified columns do not exist in the CSV file.")

            if len(columns) == 2:
                # Create a figure
                fig, ax = plt.subplots(figsize=(10, 8))

                # Plot original horizontal bars
                for col in columns:
                    ax.barh(df.index, df[col], label=col)

                # Plot inverted horizontal bars
                for col in columns:
                    inverted_data = df[col].max() - df[col]
                    ax.barh(df.index, inverted_data, label=f"Inverted {col}")

                # Add decorations
                ax.set_title('Horizontal Butterfly Plot')
                ax.legend()
                ax.set_yticks(df.index)
                ax.set_yticklabels(df.index)  # Make sure index labels are appropriate
                ax.invert_yaxis()  # Invert the y-axis for a more natural display

                # Save the image to BytesIO
                img_butterfly_horizontal_bar = BytesIO()
                plt.savefig(img_butterfly_horizontal_bar, format='png')
                plt.close()

                # Create a response with the image
                response = HttpResponse(img_butterfly_horizontal_bar.getvalue(), content_type='image/png')
                response['Content-Disposition'] = 'attachment; filename=butterfly_horizontal_bar_plot.png'

            else:
                response = HttpResponse("Please provide exactly two column names for a horizontal butterfly plot.")

            return response
    else:
        form = CSVUploadForm()

    return render(request, 'csv_graphic/graphic_functions/butterfly.html', {'form': form})


def stem(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            columns = [col.strip() for col in form.cleaned_data['column'].split(',')]

            df = pd.read_csv(csv_file)

            # Build Stem Plot
            if len(columns) == 2:
                plt.figure(figsize=(10, 8))

                x_column, y_column = columns

                plt.stem(df[x_column], df[y_column], basefmt='b-', linefmt='r-', markerfmt='ro', label=f'Stem Plot ({x_column}, {y_column})')
                plt.title('Stem Plot')
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.legend()
                plt.tight_layout()

                img_stem = BytesIO()
                plt.savefig(img_stem, format='png')
                plt.close()

                # Create a response with the image
                response = HttpResponse(img_stem.getvalue(), content_type='image/png')
                response['Content-Disposition'] = f'attachment; filename=stem_plot.png'

            else:
                response = HttpResponse("Please provide exactly two column names for a stem plot.")

            return response
    else:
        form = CSVUploadForm()

    return render(request, 'csv_graphic/graphic_functions/stem.html', {'form': form})


def bar_chart(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            columns = [col.strip() for col in form.cleaned_data['column'].split(',')]

            df = pd.read_csv(csv_file)

            # Build Bar Charts
            if len(columns) == 1:
                column_name = columns[0]
                plt.figure(figsize=(10, 6))
                counts = df[column_name].value_counts()
                counts.plot(kind='bar', color='skyblue')
                plt.title(f'Bar Chart of {column_name}')
                plt.xlabel(column_name)
                plt.ylabel('Count')
                plt.tight_layout()

                img_bar = BytesIO()
                plt.savefig(img_bar, format='png')
                plt.close()

                # Create a response with the image
                response = HttpResponse(img_bar.getvalue(), content_type='image/png')
                response['Content-Disposition'] = f'attachment; filename="{column_name}_bar_chart.png"'

            else:
                img_bar_list = []

                # Build Bar Charts for multiple columns
                for column_name in columns:
                    plt.figure(figsize=(10, 6))
                    counts = df[column_name].value_counts()
                    counts.plot(kind='bar', color='skyblue')
                    plt.title(f'Bar Chart of {column_name}')
                    plt.xlabel(column_name)
                    plt.ylabel('Count')
                    plt.tight_layout()

                    img_bar = BytesIO()
                    plt.savefig(img_bar, format='png')
                    plt.close()
                    img_bar_list.append((f'{column_name}_bar_chart.png', img_bar.getvalue()))

                # Combine all images into a single response as a zip file
                response = HttpResponse(content_type='application/zip')
                response['Content-Disposition'] = 'attachment; filename=bar_charts.zip'

                with ZipFile(response, 'w') as zip_file:
                    for img_name, img_data in img_bar_list:
                        zip_file.writestr(img_name, img_data)

            return response
    else:
        form = CSVUploadForm()

    return render(request, 'csv_graphic/graphic_functions/bar_chart.html', {'form': form})