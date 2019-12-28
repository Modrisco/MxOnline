from django.db import models

from apps.users.models import BaseModel


class City(BaseModel):
    name = models.CharField(verbose_name="city name", max_length=50)
    desc = models.TextField(verbose_name="city description")

    class Meta:
        verbose_name = "city organization"
        verbose_name_plural = verbose_name


class CourseOrg(BaseModel):
    name = models.CharField(verbose_name="org name", max_length=50)
    desc = models.TextField(verbose_name="org description")
    tag = models.CharField(verbose_name="org tag", default="World", max_length=10)
    category = models.CharField(verbose_name="org category",
                                choices=(("tafe", "tafe"), ("uni", "university"), ("indi", "individual")))
    click_nums = models.IntegerField(verbose_name="number of clicks", default=0)
    fav_nums = models.IntegerField(verbose_name="number of favorites", default=0)
    logo = models.ImageField(verbose_name="org logo", upload_to="org/%Y/%m", max_length=100)
    address = models.CharField(verbose_name="org address", max_length=150)
    students = models.IntegerField(verbose_name="number of students", default=0)
    course_nums = models.IntegerField(verbose_name="number of courses", default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="city located")

    class Meta:
        verbose_name = "course organization"
        verbose_name_plural = verbose_name


class Teacher(BaseModel):
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="teacher org")
    name = models.CharField(verbose_name="teacher name", max_length=50)
    work_years = models.IntegerField(verbose_name="work years", default=0)
    work_company = models.CharField(verbose_name="work company", max_length=50)
    work_position = models.CharField(verbose_name="work position", max_length=50)
    characteristics = models.CharField(verbose_name="teaching characteristics", max_length=50)
    click_nums = models.IntegerField(verbose_name="number of clicks", default=0)
    fav_nums = models.IntegerField(verbose_name="number of favorites", default=0)
    age = models.IntegerField(verbose_name="teacher age", default=18)
    avatar = models.ImageField(verbose_name="teacher avatar", upload_to="teacher/%Y/%m", max_length=100)

    class Meta:
        verbose_name = "course lecturer"
        verbose_name_plural = verbose_name
