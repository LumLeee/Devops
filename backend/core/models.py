from django.db import models

class StudentProfile(models.Model):
    fullname = models.CharField(max_length=200)
    student_id = models.CharField(max_length=50, unique=True)
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fullname} ({self.student_id})"
