from django.db import models
from django.db.models import Sum

class ProblemSet(models.Model):
    name = models.CharField(max_length=100)
    total_score = models.FloatField(default=0)
    total_problems = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def update_total_score(self):
        total_score = self.problems.aggregate(Sum('score'))['score__sum']
        self.total_score = total_score or 0
        self.total_problems = self.problems.count()
        self.save()

    def __str__(self):
        return self.name


class Problem(models.Model):
    problem_set = models.ForeignKey(ProblemSet, on_delete=models.CASCADE, related_name="problems")
    order = models.IntegerField()
    score = models.FloatField()
    success = models.BooleanField()
    question_text = models.TextField()

    def __str__(self):
        return f"문제 {self.order}: {self.question_text[:20]}"
