from django.shortcuts import render, redirect, get_object_or_404
from .models import ProblemSet, Problem
from .forms import ProblemSetForm, ProblemForm
from django.db.models import Max

def problem_set_list(request):
    problem_sets = ProblemSet.objects.all()
    return render(request, 'problem_set_list.html', {'problem_sets': problem_sets})

def problem_set_create(request):
    if request.method == 'POST':
        problem_set_form = ProblemSetForm(request.POST)

        if problem_set_form.is_valid():
            # 훈련 세트를 저장
            problem_set = problem_set_form.save(commit=False)
            problem_set.save()


            return redirect('problem_set_list')  # 훈련 세트 목록 페이지로 리디렉션
        else:
            # 폼이 유효하지 않으면 오류 메시지 출력
            print('ProblemSetForm Errors:', problem_set_form.errors)  # 문제 세트 폼 오류

    else:
        problem_set_form = ProblemSetForm()

    return render(request, 'problem_set_create.html', {
        'problem_set_form': problem_set_form,
    })

def problem_set_edit(request, problem_set_id):
    problem_set = ProblemSet.objects.get(id=problem_set_id)
    problems = Problem.objects.filter(problem_set=problem_set)

    # 맞은 문제와 틀린 문제 수 계산
    correct_count = problems.filter(success=True).count()
    incorrect_count = problems.filter(success=False).count()

    # 다음에 추가할 문제의 order 계산
    next_order = problems.aggregate(Max('order'))['order__max'] + 1 if problems.exists() else 1
    
    if request.method == 'POST':
        problem_form = ProblemForm(request.POST)
        if problem_form.is_valid():
            problem = problem_form.save(commit=False)
            problem.problem_set = problem_set
            problem.order = next_order  # 자동으로 order 할당
            problem.save()
            problem_set.update_score()  # 문제 세트의 총 점수 업데이트
            return redirect('problem_set_edit', problem_set.id)  # 리다이렉트 확인
        else:
            print('ProblemForm Errors:', problem_form.errors)  # 폼 오류 로그 출력
    else:
        problem_form = ProblemForm()

    return render(request, 'problem_set_edit.html', {
        'problem_set': problem_set,
        'problem_form': problem_form,
        'problems': problems,
        'next_order': next_order,  # 다음 문제의 순서를 전달
        'correct_count': correct_count,  # 맞은 문제 수 전달
        'incorrect_count': incorrect_count,  # 틀린 문제 수 전달
    })


def problem_set_delete(request, problem_set_id):
    problem_set = get_object_or_404(ProblemSet, id=problem_set_id)

    # POST 요청일 경우에만 삭제
    if request.method == 'POST':
        problem_set.delete()
        return redirect('problem_set_list')  # 문제 세트 목록 페이지로 리다이렉트

    return render(request, 'problem_set_delete.html', {
        'problem_set': problem_set
    })

def problem_delete(request, problem_id):
    # 문제 객체를 찾고, 없으면 404 오류를 반환
    problem = get_object_or_404(Problem, id=problem_id)
    
    if request.method == 'POST':
        problem_set = problem.problem_set  # 문제 세트 객체를 가져옴
        problem.delete()  # 문제 삭제
        problem_set.update_score()  # 문제 세트의 점수 업데이트
        return redirect('problem_set_edit', problem_set.id)  # 문제 세트 편집 화면으로 리다이렉트
    
    return redirect('problem_set_edit', problem.problem_set.id)  # GET 요청인 경우