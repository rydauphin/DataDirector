from .forms import FileUploadForm
from django.shortcuts import render

def fileupload2(request):
    form = FileUploadForm()
    return render(request, 'fileupload.html', {'form': form})

def fileupload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileUploadForm()
    return render(request, 'fileupload.html', {
        'form': form
    })