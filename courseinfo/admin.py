from django.contrib import admin

from .models import Semester, Section, Course, Instructor, Student, Registration, Period, Year


admin.site.register(Period)
admin.site.register(Year)
admin.site.register(Registration)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Semester)

