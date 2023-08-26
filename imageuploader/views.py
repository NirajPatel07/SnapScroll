from django.shortcuts import render
from .forms import ImageForm
from .models import Image


def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    img = Image.objects.all()
    form = ImageForm()
    return render(request, 'imageuploader/home.html', {'images': img, 'form': form})

