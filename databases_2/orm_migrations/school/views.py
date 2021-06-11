from django.views.generic import ListView
from .models import Student


class StudentListView(ListView):
    model = Student
    template = 'school/students_list.html'

    def students_list(self):
        ordering = 'group'
        students = Student.objects.order_by(ordering)
        context = {'students': students}
        return context