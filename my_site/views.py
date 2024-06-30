from audioop import reverse
from typing import TYPE_CHECKING

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from info.models import Model_Mashine_Tools
from my_site.models import User
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


# class RegisterForm(UserCreationForm):
#     pass
#
#
# class RegisterView(FormView):
#     form_class = RegisterForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('profile')
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context)
