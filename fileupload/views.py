from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

from fileupload.models import FilesUpload

# Create your views here.
def home(request):
    if request.method == "POST":
        file = request.FILES["file"]
        document = FilesUpload.objects.create(file=file)
        document.save()
        return HttpResponse("Your file was uploaded.")
    return render(request, "index.html")
