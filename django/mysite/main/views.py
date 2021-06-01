from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def homepage(request):
    return HttpResponse("butt")


def upload(request):
    return render(request=request,
                  template_name='main/upload.html'

                  )


# file upload
    # Post file to django
    # Set proper form encode type
    # enctype = 'multipart/form-data'
    # Files are uploaded to request.FILES
    # dictionary like
    # each file is an UpleadedFile instance
    # UploadedFile.read/content_type (django docs)
