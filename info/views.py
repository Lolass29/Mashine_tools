from django.shortcuts import render, redirect
from .models import Company
from .models import RegistrationForm


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


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
