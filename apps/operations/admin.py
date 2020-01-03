from django.contrib import admin

from apps.operations.models import UserAsk, UserCourses, UserFavorite, UserMessage, CourseComments


class UserAskAdmin(admin.ModelAdmin):
    list_display = ["name", "mobile", "course_name", "add_time"]
    search_fields = ["name", "mobile", "course_name"]
    list_filter = ["name", "mobile", "course_name", "add_time"]


class UserCoursesAdmin(admin.ModelAdmin):
    list_display = ["user", "course", "add_time"]
    search_fields = ["user", "course"]
    list_filter = ["user", "course", "add_time"]


class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ["user", "fav_id", "fav_type", "add_time"]
    search_fields = ["user", "fav_id", "fav_type"]
    list_filter = ["user", "fav_id", "fav_type", "add_time"]


class UserMessageAdmin(admin.ModelAdmin):
    list_display = ["user", "has_read", "message", "add_time"]
    search_fields = ["user", "has_read", "message"]
    list_filter = ["user", "has_read", "message", "add_time"]


class CourseCommentsAdmin(admin.ModelAdmin):
    list_display = ["user", "course", "comment", "add_time"]
    search_fields = ["user", "course", "comment"]
    list_filter = ["user", "course", "comment", "add_time"]


admin.site.register(UserAsk, UserAskAdmin)
admin.site.register(UserCourses, UserCoursesAdmin)
admin.site.register(UserFavorite, UserFavoriteAdmin)
admin.site.register(UserMessage, UserMessageAdmin)
admin.site.register(CourseComments, CourseCommentsAdmin)
