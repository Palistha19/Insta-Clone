from django.shortcuts import render

# Create your views here.


def delete_photos(req,ID):
    photos=Photos.objects.get(id=ID)
    photos.delete()
    return redirect("photos_home")

