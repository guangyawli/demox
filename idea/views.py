from django.shortcuts import render, redirect

from .forms import FileUploadModelForm
from .models import File
# Create your views here.


def index(request):
    return render(request, 'idea/index.html', locals())


def file_list(request):
    files = File.objects.all().order_by("-id")
    return render(request, 'idea/file_list.html', {'files': files})


def model_form_upload(request):
    if request.method == "POST":
        form = FileUploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("file_list")
    else:
        form = FileUploadModelForm()

    return render(request, 'idea/upload_form.html', {'form': form,
                                                            'heading': 'Upload files with ModelForm'})