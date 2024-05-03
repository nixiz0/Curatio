from django.shortcuts import render
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

from panel.forms import CSVUploadForm


# Create your views here.
def graphic(request):
    return render(request, "graphic.html")

def graphic_import_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            file_name = csv_file.name
            df = pd.read_csv(csv_file)
            
            # Build Pie Chart
            img_pie = BytesIO()
            plt.figure(figsize=(5, 4))
            type_counts = df.dtypes.value_counts()
            plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140)
            plt.title('Distribution of Types')
            plt.tight_layout()
            plt.savefig(img_pie, format='png')
            plt.close()
            img_pie64 = base64.b64encode(img_pie.getvalue()).decode('utf-8')

            # Build Histogram
            img_hist = BytesIO()
            plt.figure(figsize=(8, 4)) 
            df.hist()
            plt.tight_layout() 
            plt.savefig(img_hist, format='png')
            plt.close()
            img_hist64 = base64.b64encode(img_hist.getvalue()).decode('utf-8')
            
            # Build Heatmap
            img_heatmap = BytesIO()
            plt.figure(figsize=(8, 4)) 
            numeric_columns = df.select_dtypes(include=['number'])
            sns.heatmap(data=numeric_columns.corr(), annot=True, cmap='coolwarm')
            plt.title('Heatmap of correlation')
            plt.tight_layout() 
            plt.savefig(img_heatmap, format='png')
            plt.close()
            img_heatmap64 = base64.b64encode(img_heatmap.getvalue()).decode('utf-8')

            # Build Boxplot
            img_boxplot = BytesIO()
            plt.figure()
            plt.figure(figsize=(8, 4)) 
            sns.boxplot(data=df)
            plt.title('General Boxplot')
            plt.tight_layout()
            plt.savefig(img_boxplot, format='png')
            plt.close()
            img_boxplot64 = base64.b64encode(img_boxplot.getvalue()).decode('utf-8')

            return render(request, 'graphic.html', {'df': df, 'file_name': file_name, 'img_hist': img_hist64,
                                    'img_boxplot': img_boxplot64, 'img_pie': img_pie64, 'img_heatmap64':img_heatmap64})
    else:
        form = CSVUploadForm()
    return render(request, 'csv_graphic/upload.html', {'form': form})