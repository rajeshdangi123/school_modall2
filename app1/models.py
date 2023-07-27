from django.db import models


class School(models.Model):
    school_name = models.CharField(max_length=60, blank=True, null=True)
    teacher_strength = models.CharField(max_length=20, blank=True, null=True)
    class_strength = models.CharField(max_length=20, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)

    # established_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    # class_name=models.CharField(max_length=15,)
    def __str__(self) -> str:
        return self.school_name


class Student(models.Model):
    enrollment_number = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    class_name1 = models.CharField(max_length=20, blank=True, null=True)
    School_name1 = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="comments_rel"
    )

    def __str__(self) -> str:
        return self.first_name


# Create your models here.
