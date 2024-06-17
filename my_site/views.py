from typing import TYPE_CHECKING
from django.shortcuts import render, HttpResponse
from info.models import Model_Mashine_Tools

if TYPE_CHECKING:
    from django.http import HttpRequest


def my_site_view(request):
    my_info_objects = Model_Mashine_Tools.objects.all()
    return render(request, 'Product.html', {'my_info_objects': my_info_objects})
