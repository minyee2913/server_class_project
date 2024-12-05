from django.shortcuts import render

from .models import ProblemSet, Problem

# Create your views here.
def index(request):
    sets = ProblemSet.objects.all()
    cells = Problem.objects.all()

    return render(request,'main/index.html', {'sets': sets, 'cells': cells})