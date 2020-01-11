from django.shortcuts import render

# Create your views here.

def get_add_photos(req):
    return render(req,'add_photos.html')


def post_add_photos(req):
    label=req.POST["label"]
    caption=req.POST["caption"]

    image=req.FILES['photo']
    fs=FileSystemStorage()
    filename=fs.save(image.name,image)
    url=fs.url(filename)


    new_photos=Photos(label=label,caption=caption,photo=url)
    new_photos.save()

    return redirect('photos_home')

def get_photos_home(req):
    all_photos=Photos.objects.all()
    if 'query_lable' in req.GET:
        all_photos=Photos.objects.filter(label=req.GET['query_lable'])

    context={
        "photos":all_photos
    }
    return render(req,'photos_home.html',context=context)