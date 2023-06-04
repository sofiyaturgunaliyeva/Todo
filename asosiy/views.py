from django.shortcuts import render,redirect
from.models import *

def home(sorov):
    if sorov.method == 'POST':
        Reja.objects.create(
            sarlavha=sorov.POST.get('sarlavha'),
            tavsif=sorov.POST.get('batafsil'),
            holat=sorov.POST.get('holat'),
            vaqt=sorov.POST.get('vaqt')
        )

        return redirect('/')
    content = {
        "rejalar": Reja.objects.all()
    }
    return render(sorov,'todo_eski (2).html',content)


def reja_ochir(sorov, son):
    Reja.objects.get(id=son).delete()
    return redirect('/')