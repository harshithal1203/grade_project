from django.shortcuts import render
from .models import Student

# Create your views here.
def grade_distribution(request):
    students = Student.objects.all()

    count_A = sum(1 for s in students if s.grade() == 'A')
    count_B = sum(1 for s in students if s.grade() == 'B')
    count_C = sum(1 for s in students if s.grade() == 'C')
    count_D = sum(1 for s in students if s.grade() == 'D')
    count_Fail = sum(1 for s in students if s.grade() == 'Fail')

    total = students.count()

    context = {
        'count_A': count_A,
        'count_B': count_B,
        'count_C': count_C,
        'count_D': count_D,
        'count_Fail': count_Fail,
        'total': total,
        'students': students
    }

    return render(request, 'grade_distribution.html', context)


