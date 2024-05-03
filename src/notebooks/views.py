import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .functions.classic_notebook import create_notebook


# Create your views here.
def notebooks(request):
    return render(request, "notebooks.html")

@csrf_exempt
def classic_notebooks(request):
    if request.method == 'POST':
        try:
            filename = 'base_notebook.ipynb'
            create_notebook(filename)
            filepath = os.path.join(settings.MEDIA_ROOT, filename)
            with open(filepath, 'rb') as f:
                file_data = f.read()
            response = HttpResponse(file_data, content_type='application/force-download')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            
            # Delete file after sending response
            os.remove(filepath)
            
            return response
        except Exception as e:
            return render(request, 'notebooks.html', {'error': str(e)})
    else:
        return render(request, 'notebooks.html')