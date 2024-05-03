import os
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from ydata_profiling import ProfileReport
import sweetviz as sv

from panel.forms import CSVUploadForm


# Create your views here.
def auto_explo(request):
    return render(request, "auto_explo.html")

def ydata_explo(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            
            df = pd.read_csv(csv_file)
            profile = ProfileReport(df, title="Profiling Report")
            profile_file_path = "report-profiling.html"
            profile.to_file(profile_file_path)

            with open(profile_file_path, 'rb') as file:
                html_content = file.read()

            os.remove(profile_file_path)
            response = HttpResponse(html_content, content_type='text/html')
            response['Content-Disposition'] = f'attachment; filename="{profile_file_path}"'

            return response
    else:
        form = CSVUploadForm()
    return render(request, 'csv_auto_explo/ydata_explo.html', {'form': form})

def sweetviz_explo(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            
            df = pd.read_csv(csv_file)
            
            report_sv = sv.analyze(df)
            report_sv_file_path = "sweetviz-report.html"
            report_sv.show_html(report_sv_file_path)

            with open(report_sv_file_path, 'r') as file:
                html_content = file.read()

            os.remove(report_sv_file_path)
            response = HttpResponse(html_content, content_type='text/html')
            response['Content-Disposition'] = f'attachment; filename="{report_sv_file_path}"'

            return response
    else:
        form = CSVUploadForm()
    return render(request, 'csv_auto_explo/sweetviz_explo.html', {'form': form})