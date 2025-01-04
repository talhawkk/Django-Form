from django.contrib import admin
from home.models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','stuid','stuname','stuemail','stupass')


# admin.site.register(Student,StudentAdmin)
