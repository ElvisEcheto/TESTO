from django.shortcuts import render

from packages.models import Package

from .forms import PackageForm

def create_package(request):
    form = PackageForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('packages')    
    return render(request, 'packages/create.html', {'form': form})

def packages(request):
    return render(request, 'packages/index.html')
from django.shortcuts import render, redirect

def package(request):    
    package_list = Package.objects.all()    
    return render(request, 'packages/index.html', {'package_list': package_list})

def change_status_package(request, packages_id):
    package = Package.objects.get(pk=packages_id)
    package.status = not package.status
    package.save()
    return redirect('package')