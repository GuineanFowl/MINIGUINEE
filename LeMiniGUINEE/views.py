from django.shortcuts import render, redirect

from Element.models import Categorie, Element

from .forms import SignupForm

def index(request):
    elements = Element.objects.filter(est_vendu=False)[0:20]
    categories = Categorie.objects.all()

    return render(request, 'LeMiniGUINEE/index.html', {
        'categories': categories,
        'elements': elements,
    })


def contact(request):
    return render(request, 'LeMiniGUINEE/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()
            
    return render(request, 'LeMiniGUINEE/signup.html', {
        'form': form
    })