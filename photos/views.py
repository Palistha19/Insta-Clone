from django.shortcuts import render

# Create your views here.


def delete_photos(req,ID):
    photos=Photos.objects.get(id=ID)
    photos.delete()
    return redirect("photos_home")

def get_photos_home(req):
    all_photos=Photos.objects.all()
    if 'query_lable' in req.GET:
        all_photos=Photos.objects.filter(label=req.GET['query_lable'])

    context={
        "photos":all_photos
    }
    return render(req,'photos_home.html',context=context)