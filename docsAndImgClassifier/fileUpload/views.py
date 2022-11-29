from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import TemplateView
from .forms import UploadFileForm
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


def handle_uploaded_file(f):
    print("upload,POS!!T", f)
    with open('AD@name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload(request):
    print("upload,request", request)
    if request.method == 'POST':
        print("upload,POST", request.FILES)
        form = UploadFileForm(request.POST, request.FILES)
        print("upload,form")
        if form.is_bound:
            print("upload,is_valid")
            handle_uploaded_file(request.FILES['files'])
            return HttpResponseRedirect('/success/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
