from django.shortcuts import render

# Create your views here.
def get_update_photos(req,ID):
    photos=Photos.objects.get(id=ID)
    context={
        "photos":photos
    }
    return render(req,"update_photos.html",context=context)

def post_update_photos(req,ID):
    label=req.POST["label"]
    caption=req.POST["caption"]

    image=req.FILES['photo']
    fs=FileSystemStorage()
    filename=fs.save(image.name,image)
    url=fs.url(filename)

