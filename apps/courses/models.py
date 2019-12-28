from datetime import datetime

from django.db import models

from apps.users.models import BaseModel
from apps.organizations.models import Teacher


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, verbose_name="course lecturer", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="course name", max_length=50)
    desc = models.CharField(verbose_name="course description", max_length=300)
    learning_time = models.IntegerField(verbose_name="learning time in seconds", default=0)
    degree = models.CharField(verbose_name="course difficulty",
                              choices=(("junior", "junior"), ("mid", "mid"), ("senior", "senior")), max_length=6)
    students = models.IntegerField(verbose_name="number of students", default=0)
    fav_nums = models.IntegerField(verbose_name="number of favorites", default=0)
    click_nums = models.IntegerField(verbose_name="number of clicks", default=0)
    category = models.CharField(verbose_name="course category", max_length=20, default="backend development")
    tag = models.CharField(verbose_name="course tag", max_length=10, default="")
    you_need_know = models.CharField(verbose_name="course instruction", max_length=300, default="")
    teacher_tell = models.CharField(verbose_name="teacher's introduction", max_length=300, default="")

    detail = models.TextField(verbose_name="course detail")
    image = models.ImageField(verbose_name="course image", upload_to="course/%Y/%m", max_length=100)

    class Meta:
        verbose_name = "course information"
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return


class Chapter(BaseModel):
    # on_delete: CASCADE different from SET_NULL
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="chapter name", max_length=100)
    learning_time = models.IntegerField(verbose_name="learning time in seconds", default=0)

    class Meta:
        verbose_name = "chapter information"
        verbose_name_plural = verbose_name


class Lesson(BaseModel):
    # on_delete: CASCADE different from SET_NULL
    lesson = models.ForeignKey(Chapter, verbose_name="lesson", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="lesson name", max_length=100)
    learning_time = models.IntegerField(verbose_name="learning time in seconds", default=0)
    url = models.CharField(verbose_name="video link", max_length=200)

    class Meta:
        verbose_name = "video information"
        verbose_name_plural = verbose_name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="course")
    name = models.CharField(verbose_name="resource name", max_length=100)
    file = models.FileField(verbose_name="resource download link", upload_to="course/resource/%Y/%m")

    class Meta:
        verbose_name = "course resource"
        verbose_name_plural = verbose_name
