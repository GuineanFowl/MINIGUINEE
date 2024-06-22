from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from Element.models import Element

@login_required
def index(request):
    elements = Element.objects.filter(creer_par=request.user)

    return render(request, 'dashboard/index.html', {
        'elements': elements,
    })




