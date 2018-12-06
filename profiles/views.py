from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .models import File as FileModel
# Create your views herssse.ss
def upload(request):
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage("files/")
        filename = fs.save(myfile.name, myfile)
        fileModel = FileModel(upload=myfile.name)
        fileModel.save()
        fs.url(filename)
        return redirect('index')
    else:
        return render(request, 'profiles/upload.html')


def index(request):
    return render(request, "profiles/index.html")

def login(request):
    return render(request, "profiles/index.html")