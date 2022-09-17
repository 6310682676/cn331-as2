from django.db import models

# Create your models here.

class Subject(models.Model):
    subjectCode = models.CharField(max_length=64)
    subjectName = models.CharField(max_length=64)
    semester = models.IntegerField()
    year = models.IntegerField()
    quota = models.IntegerField()
    status = models.BooleanField(default=True)
    detail = models.CharField(max_length=99999, default="")
    def __str__(self):
        return f'{self.subjectCode} {self.subjectName} semester:{self.semester} year:{self.year} quota:{self.quota}'