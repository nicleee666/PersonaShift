from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import ImageModel
from django.contrib import messages

def home_view(request):
    # Your logic here, for example, a simple render:
    return render(request, 'image_editor/home.html')

def image_upload_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the form along with the image
            messages.success(request, 'Image uploaded successfully!')
            return redirect('home')  # Redirect to a success page or some other page
    else:
        form = ImageUploadForm()

    return render(request, 'image_editor/upload.html', {'form': form})
