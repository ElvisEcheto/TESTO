from django.shortcuts import render, redirect

from facilities.models import Facilitie

def facilities(request):    
    facilities_list = Facilitie.objects.all()    
    return render(request, 'facilities/index.html', {'facilities_list': facilities_list})

def change_status_facilitie(request, facilitie_id):
    facilitie = Facilitie.objects.get(pk=facilitie_id)
    facilitie.status = not facilitie.status
    facilitie.save()
    return redirect('facilities')
