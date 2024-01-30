from django.shortcuts import render, redirect

from typedocuments.models import Typedocument

from django.http import JsonResponse

from django.contrib import messages

from .forms import TypedocumentForm

def create_typedocument(request):
    form = TypedocumentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('typedocuments')    
    return render(request, 'typedocuments/create.html', {'form': form})

def typedocuments(request):    
    typedocuments_list = Typedocument.objects.all()    
    return render(request, 'typedocuments/index.html', {'typedocuments_list': typedocuments_list})

def change_status_typedocument(request, typedocument_id):
    typedocument = Typedocument.objects.get(pk=typedocument_id)
    typedocument.status = not typedocument.status
    typedocument.save()
    return redirect('typedocuments')

def detail_typedocument(request, typedocument_id):
    typedocument = Typedocument.objects.get(pk=typedocument_id)
    data = { 'name': typedocument.name, 'acronyms' : typedocument.acronyms }    
    return JsonResponse(data)


def delete_typedocument(request, typedocument_id):
    typedocument = Typedocument.objects.get(pk=typedocument_id)
    try:
        typedocument.delete()        
        messages.success(request, 'tipo documento eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar el autor porque está asociado a un libro.')
    return redirect('typedocuments')