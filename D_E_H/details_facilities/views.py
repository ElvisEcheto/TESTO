from django.shortcuts import render, redirect

from details_facilities.models import Details_Facilitie

from .forms import Details_FacilitieForm

def create_details_facilitie(request):
    form = Details_FacilitieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('details_facilities')    
    return render(request, 'details_facilities/create.html', {'form': form})

def details_facilities(request):    
    details_facilities_list = Details_Facilitie.objects.all()    
    return render(request, 'details_facilities/index.html', {'details_facilities_list': details_facilities_list})

def change_status_details_facilitie(request, details_facilitie_id):
    details_facilitie = details_facilitie.objects.get(pk=details_facilitie_id)
    details_facilitie.status = not details_facilitie.status
    details_facilitie.save()
    return redirect('details_facilities')
