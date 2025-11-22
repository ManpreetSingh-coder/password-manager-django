from django.shortcuts import render, redirect
from .models import password


def dashboard(request):
    passwords = password.objects.all().order_by('-id')
    return render(request, 'dashboard.html', {'data': passwords})


def add_password(request):
    if request.method == "POST":
        website = request.POST.get('Website_name')
        username_value = request.POST.get('Username_Email', '')
        password_value = request.POST.get('password')

        if website and password_value:
            password.objects.create(
                website=website,
                username=username_value,
                password=password_value
            )
            return redirect('dashboard')
    
    return render(request, 'add_password.html')


def delete_password(request, id):
    entry = password.objects.get(id=id)
    entry.delete()
    return redirect('dashboard')


