from django.contrib import admin

# Register your models here.
from app1.models import School, Student


class SchoolAdmin(admin.ModelAdmin):
    list_display = "school_name", "teacher_strength", "class_strength", "contact_number"


admin.site.register(School, SchoolAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "enrollment_number",
        "first_name",
        "last_name",
        "class_name1",
        "School_name1",
    )


admin.site.register(Student, StudentAdmin)
