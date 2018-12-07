from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .models import File as FileModel
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here

def index(request):
    arturs_files = FileModel.objects.filter(user='3')
    mamas_files = FileModel.objects.filter(user='2')
    tata_files = FileModel.objects.filter(user='1')
    print(arturs_files)
    context = {
        'artur_files':arturs_files,
        'mama_files':mamas_files,
        'tata_files':tata_files,
    }
    return render(request, "profiles/index.html",context)


def upload(request):
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage("files/")
        filename = fs.save(myfile.name, myfile)
        fileModel = FileModel(upload=myfile.name,user=request.user)
        fileModel.save()
        fs.url(filename)
        return redirect('index')
    else:
        return render(request, 'profiles/upload.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']    
        
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return redirect('loguj')
    else:
        return render(request, "profiles/login.html")