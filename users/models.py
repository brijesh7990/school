from django.contrib.auth.models import AbstractUser
from django.db import models
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from users.manager import CustomUserManager


# Create your models here.


class CustomUser(AbstractUser, BaseModel):
    SUPERADMIN = "superadmin"
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"
    PARENT = "parent"

    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

    APOS = "A+"
    ANEG = "A-"
    BPOS = "B+"
    BNEG = "B-"
    OPOS = "O+"
    ONEG = "O-"
    APPOS = "AP+"
    APNEG = "AP-"

    role_data = (
        (SUPERADMIN, "SuperAdmin"),
        (ADMIN, "Admin"),
        (TEACHER, "Teacher"),
        (STUDENT, "Student"),
        (PARENT, "Parent"),
    )
    gender_data = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    )

    blood_group_data = (
        (APOS, "A+"),
        (ANEG, "A-"),
        (BPOS, "B+"),
        (BNEG, "B-"),
        (OPOS, "O+"),
        (ONEG, "O-"),
        (APPOS, "AB+"),
        (APNEG, "AB-"),
    )

    dob = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_data, null=True, blank=True)
    blood_group = models.CharField(
        max_length=25, choices=blood_group_data, null=True, blank=True
    )
    phone = models.CharField(max_length=15, null=True, blank=True)
    religion = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    role = models.CharField(max_length=25, choices=role_data)
    profile_pic = models.ImageField(
        upload_to="media/profilepics", null=True, blank=True
    )
    email = models.EmailField(_("email address"), unique=True)

    def __str__(self):
        return self.username

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password", "role"]

    objects = CustomUserManager()


class Admin(BaseModel):
    user = models.OneToOneField("users.CustomUser", on_delete=models.CASCADE)
    school = models.ForeignKey(
        "school.School", on_delete=models.CASCADE, related_name="school_admin"
    )


class Student(BaseModel):
    user = models.OneToOneField("users.CustomUser", on_delete=models.CASCADE)
    school = models.ForeignKey(
        "school.School", on_delete=models.CASCADE, related_name="school_student"
    )
    standard = models.ForeignKey(
        "academic.Standard", on_delete=models.CASCADE, related_name="standard_student"
    )
    section = models.ForeignKey(
        "academic.Section", on_delete=models.CASCADE, related_name="section_student"
    )


class Teacher(BaseModel):
    user = models.OneToOneField("users.CustomUser", on_delete=models.CASCADE)
    joining_date = models.DateTimeField()
    school = models.ForeignKey(
        "school.School", on_delete=models.CASCADE, related_name="school_teacher"
    )


class Parent(BaseModel):
    user = models.OneToOneField("users.CustomUser", on_delete=models.CASCADE)
    school = models.ForeignKey(
        "school.School", on_delete=models.CASCADE, related_name="school_parent"
    )
    student = models.ManyToManyField("users.Student")


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == CustomUser.STUDENT:
            Student.objects.create(user=instance)
        elif instance.role == CustomUser.TEACHER:
            Teacher.objects.create(user=instance)
        elif instance.role == CustomUser.PARENT:
            Parent.objects.create(user=instance)
        elif instance.role == CustomUser.ADMIN:
            Admin.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.role == CustomUser.STUDENT:
        instance.student.save()
    elif instance.role == CustomUser.TEACHER:
        instance.teacher.save()
    elif instance.role == CustomUser.PARENT:
        instance.parent.save()
    elif instance.role == CustomUser.ADMIN:
        instance.admin.save()
