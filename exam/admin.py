from django.contrib import admin
from .models import Course,Semester,Student,Faculty,Batch,ExamResult


admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Batch)
admin.site.register(ExamResult)
