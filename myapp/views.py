from django.shortcuts import render
from .models import *
from .photo import *
from django.http import HttpResponse

def home(request):
    if request.method=='POST':
        a=request.POST['name']
        b=request.FILES['img']
        f=Db(name=a,img=b)
        f.save()
        a=pic(b)
        if a==False:
            return HttpResponse("<html><body><h3>Please Upload another picture. This picture dimension is not compatible with our model.</h3></body></html>")
        return render(request,'home.html',{'f':f})
    return render(request,'home.html')
