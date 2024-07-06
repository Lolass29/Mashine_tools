from typing import TYPE_CHECKING
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from info.models import Model_Mashine_Tools
from my_site.forms import UserRegistrationForm
from django.http import HttpResponseRedirect

if TYPE_CHECKING:
    from django.http import HttpRequest


def my_site_view(request):
    my_info_objects = Model_Mashine_Tools.objects.all()
    return render(request, 'Product.html', {'my_info_objects': my_info_objects})


@login_required
def profile_view(request):
    return render(request, 'web/profile.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.image = request.FILES.get('image')
            user.save()
            return HttpResponseRedirect(reverse_lazy('login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
