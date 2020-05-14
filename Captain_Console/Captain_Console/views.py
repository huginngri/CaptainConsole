from django.shortcuts import render

from error_and_success import cases


def about(request):
    return render(request, 'about_us.html', cases.get_profile(dict(), request))