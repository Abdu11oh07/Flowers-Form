from django.shortcuts import render, get_object_or_404
from .models import Turlar, Gullar
from .form import GullarForm

def index(request):
    turlar = Turlar.objects.all()
    gullar = Gullar.objects.all()
    context = {
        "turlar": turlar,
        "gullar": gullar
    }
    return render(request, 'app/type.html', context)

def posts_by_turlar(request, turlar_id):
    turlar = get_object_or_404(Turlar, id=turlar_id)
    gullar = Gullar.objects.filter(type_id=turlar_id)
    context = {
        "turlar": turlar,
        "gullar": gullar
    }
    return render(request, 'app/type.html', context)

def posts_by_gullar(request, gullar_id):
    gul = get_object_or_404(Gullar, id=gullar_id)
    context = {
        'gul': gul
    }
    return render(request, 'app/gulllar_detail.html', context)

def add_post(request, ):
    if request.method == 'POST':
        form = GullarForm(data=request.POST)
        if form.is_valid():
            lesson = Gullar.objects.create(
                **form.cleaned_data
            )
            print(lesson, "Qo'shildi!")

    form = GullarForm()
    context = {
        "form": form
    }
    return render(request, 'blok/add_post.html', context)