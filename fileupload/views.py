from .forms import FileUploadForm
from django.shortcuts import render
from django.contrib import messages


def fileupload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
        else:
            messages.error(request, 'Yikes! Something went wrong!')


    else:
        form = FileUploadForm()
    return render(request, 'fileupload.html', {
        'form': form
    })