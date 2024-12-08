# views.py
from django.shortcuts import render, redirect
from .models import ProblemSet, Problem
from .forms import ProblemSetForm, ProblemForm

def problem_set_list(request):
    problem_sets = ProblemSet.objects.all()
    return render(request, 'problem_set_list.html', {'problem_sets': problem_sets})

def problem_set_create(request):
    if request.method == 'POST':
        form = ProblemSetForm(request.POST)
        if form.is_valid():
            problem_set = form.save()
            return redirect('problem_set_edit', problem_set.id)
    else:
        form = ProblemSetForm()
    return render(request, 'problem_set_create.html', {'form': form})

def problem_set_edit(request, problem_set_id):
    problem_set = ProblemSet.objects.get(id=problem_set_id)
    problems = Problem.objects.filter(problem_set=problem_set)
    if request.method == 'POST':
        problem_form = ProblemForm(request.POST)
        if problem_form.is_valid():
            problem = problem_form.save(commit=False)
            problem.problem_set = problem_set
            problem.save()
            problem_set.update_total_score()
            return redirect('problem_set_edit', problem_set.id)
    else:
        problem_form = ProblemForm()

    return render(request, 'problem_set_edit.html', {
        'problem_set': problem_set,
        'problem_form': problem_form,
        'problems': problems,
    })
