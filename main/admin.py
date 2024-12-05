from django.contrib import admin

# Register your models here.
from .models import ProblemSet, Problem

admin.site.register(ProblemSet)
admin.site.register(Problem)