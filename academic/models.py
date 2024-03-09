from django.db import models

from base.models import BaseModel


# Create your models here.


class Standard(BaseModel):
    standard = models.CharField(max_length=50)
    numeric_standard = models.IntegerField()
    teacher = models.OneToOneField(
        "users.Teacher", on_delete=models.SET_NULL, null=True
    )
    note = models.TextField(null=True, blank=True)
    subject = models.ManyToManyField("academic.Subject")

    def __str__(self):
        return self.standard


class Section(BaseModel):
    name = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    standard = models.ForeignKey("academic.Standard", on_delete=models.CASCADE)
    teacher = models.OneToOneField(
        "users.Teacher", on_delete=models.SET_NULL, null=True
    )
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Subject(BaseModel):
    subject_code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    teacher = models.ManyToManyField("users.Teacher")
    passing_mark = models.FloatField()
    total_mark = models.IntegerField()


class Syllabus(BaseModel):
    standard = models.ForeignKey("academic.Standard", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    subject = models.ForeignKey("academic.Subject", on_delete=models.CASCADE)
    file = models.FileField(upload_to="media/syllabus")

    def __str__(self):
        return self.title


class Assignment(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField()
    standard = models.ForeignKey("academic.Standard", on_delete=models.CASCADE)
    section = models.ForeignKey("academic.Section", on_delete=models.CASCADE)
    subject = models.ForeignKey("academic.Subject", on_delete=models.CASCADE)
    file = models.FileField(upload_to="media/assignment")
