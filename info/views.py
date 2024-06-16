from django.shortcuts import render
from .models import Company


def image_view(request):
    if request.method == 'POST':
        form = Company(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # дальнейшая логика
    else:
        form = Company()

    context = {
        'form': form
    }
    return render(request, 'image.html', context)
