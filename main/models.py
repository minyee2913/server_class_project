from django.db import models

class ProblemSet(models.Model):
    name = models.CharField(max_length=100)
    default_total_score = models.IntegerField(default=100)
    total_score = models.IntegerField(default=0)
    total_problems = models.IntegerField(default=20)
    correct_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def initScore(self):
        self.total_score = self.default_total_score
    
    def update_score(self):
        # 문제 세트에 관련된 문제들의 점수를 합산하고, 맞은 문제 수를 계산하는 로직
        problems = self.problems.all()
        total_score = self.default_total_score

        for problem in problems:
            if not problem.success:
                total_score = total_score - problem.score

        self.total_score = total_score
        self.save()

    def __str__(self):
        return self.name

class Problem(models.Model):
    problem_set = models.ForeignKey(ProblemSet, related_name='problems', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    score = models.IntegerField()
    success = models.BooleanField(default=False)
    order = models.IntegerField()

    def __str__(self):
        return self.question_text
