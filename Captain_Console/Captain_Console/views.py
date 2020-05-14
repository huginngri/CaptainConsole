from django.shortcuts import render, redirect

def about(request):
    return render(request, 'about_us.html')