from django.shortcuts import render
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
import json

from panel.forms import CSVUploadForm


# Create your views here.
def statistic(request):
    return render(request, "statistic.html")

def statistic_import_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            
            # Get the file name
            file_name = csv_file.name

            # Read the contents of the CSV file using pandas 
            df = pd.read_csv(csv_file)
            
            df_stat = df.describe()
            
            # Create histograms & Boxplots for numeric columns
            numeric_columns = df.select_dtypes(include='number').columns
            histograms = {}
            boxplots = {}

            for col in numeric_columns:
                plt.figure()
                df[col].plot(kind='hist', title=f'Histogram for {col}')
                plt.xlabel(col)
                plt.ylabel('Frequency')

                # Save the histogram plot as BytesIO
                image_stream = BytesIO()
                plt.savefig(image_stream, format='png')
                plt.close()

                # Convert BytesIO to base64 encoding
                image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')
                histograms[col] = image_base64

                # Create boxplot
                plt.figure()
                df[col].plot(kind='box', title=f'Boxplot for {col}', color='green')

                # Save the boxplot as BytesIO
                image_stream = BytesIO()
                plt.savefig(image_stream, format='png')
                plt.close()

                # Convert BytesIO to base64 encoding
                image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')
                boxplots[col] = image_base64
                
                # Statistic View
                quartiles = []
                mean_stds = []
                min_maxs = []
                for col in numeric_columns:
                    quartiles.append({
                        'column': col,
                        'Q1': df[col].quantile(0.25),
                        'Q2': df[col].quantile(0.5),
                        'Q3': df[col].quantile(0.75),
                        'Q4': df[col].quantile(0.9),
                    })
                    mean_stds.append({
                        'column': col,
                        'mean': df[col].mean(),
                        'var': df[col].var(),
                        'std': df[col].std(),
                    })
                    min_maxs.append({
                        'column': col,
                        'min': df[col].min(),
                        'max': df[col].max(),
                    })

            return render(request, 'statistic.html', {'df':df, 'file_name':file_name, 'df_stat':df_stat, 
                                                      'numeric_columns':numeric_columns, 'histograms': json.dumps(histograms),
                                                      'boxplots': json.dumps(boxplots), 'quartiles':quartiles, 
                                                      'mean_stds':mean_stds, 'min_maxs':min_maxs})
    else:
        form = CSVUploadForm()
    return render(request, 'csv_statistic/upload.html', {'form': form})