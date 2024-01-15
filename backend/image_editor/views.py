from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import ImageModel

def image_upload_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_success')  # Redirect to a success page.
    else:
        form = ImageUploadForm()
    return render(request, 'image_editor/upload.html', {'form': form})
