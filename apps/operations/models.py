from django.db import models
from django.contrib.auth import get_user_model

from apps.users.models import BaseModel
from apps.courses.models import Course

UserProfile = get_user_model()


class UserAsk(BaseModel):
    name = models.CharField(verbose_name="user name", max_length=20)
    mobile = models.CharField(verbose_name="user mobile number", max_length=12)
    course_name = models.CharField(verbose_name="course name", max_length=50)

    class Meta:
        verbose_name = "user ask questions"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{name}_{course} ({mobile})".format(name=self.name, course=self.course_name, mobile=self.mobile)


class CourseComments(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="user")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="course")
    comment = models.CharField(verbose_name="course comment", max_length=200)

    class Meta:
        verbose_name = "course comment"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comment


class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="user")
    fav_id = models.IntegerField(verbose_name="fav id")
    fav_type = models.IntegerField(choices=((1, "course"), (2, "org"), (3, "teacher")), default=1,
                                   verbose_name="fav type")

    class Meta:
        verbose_name = "user favorite"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{user}_{id}".format(user=self.user.name, id=self.fav_id)


class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="user")
    message = models.CharField(verbose_name="message", max_length=200)
    has_read = models.BooleanField(verbose_name="has read message", default=False)

    class Meta:
        verbose_name = "user message"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class UserCourses(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="user")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="course")

    class Meta:
        verbose_name = "user courses"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name
