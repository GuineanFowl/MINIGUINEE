from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Categorie, Element

def elements(request):
    query = request.GET.get('query', '')
    categorie_id = request.GET.get('categorie', 0)
    categories = Categorie.objects.all()
    elements = Element.objects.filter(est_vendu=False)

    if categorie_id:
        elements = elements.filter(categorie_id=categorie_id)

    if query:
        elements = elements.filter(Q(nom__icontains=query)) | (Q(description__icontains=query))

    return render(request, 'element/elements.html', {
        'elements': elements,
        'query': query,
        'categories': categories,
        'categorie_id': int(categorie_id)
    })

def detail(request, pk):
    element = get_object_or_404(Element, pk=pk)
    elements_connexes = Element.objects.filter(categorie=element.categorie, est_vendu=False).exclude(pk=pk)[0:6]

    return render(request, 'Element/detail.html', {
        'element': element,
        'elements_connexes' : elements_connexes
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            element = form.save(commit=False)
            element.creer_par = request.user
            element.save()

            return redirect('element:detail', pk=element.id)
    else:
        form = NewItemForm()

    return render(request, 'element/form.html', {
        'form': form,
        'title': 'Nouvel Element',
    })

@login_required
def edit(request, pk):
    element = get_object_or_404(Element, pk=pk, creer_par=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=element)

        if form.is_valid():
            form.save()

            return redirect('element:detail', pk=element.id)
    else:
        form = EditItemForm(instance=element)

    return render(request, 'element/form.html', {
        'form': form,
        'title': 'Editer Element',
    })


@login_required
def delete(request, pk):
    element = get_object_or_404(Element, pk=pk, creer_par=request.user)
    element.delete()

    return redirect('dashboard:index')
