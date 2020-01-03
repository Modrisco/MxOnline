from django.contrib import admin

from apps.courses.models import Course, Lesson, Chapter, CourseResource


class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "desc", "detail", "degree", "learning_time", "students"]
    search_fields = ["name", "desc", "detail", "degree", "students"]
    list_filter = ["name", "teacher__name", "desc", "detail", "degree", "students", "learning_time"]
    list_editable = ["degree", "desc"]


class LessonAdmin(admin.ModelAdmin):
    list_display = ["lesson", "name", "add_time"]
    search_fields = ["lesson", "name"]
    list_filter = ["lesson", "name", "add_time"]


class ChapterAdmin(admin.ModelAdmin):
    list_display = ["course", "name", "add_time"]
    search_fields = ["course", "name"]
    list_filter = ["course__name", "name", "add_time"]


class CourseResourceAdmin(admin.ModelAdmin):
    list_display = ["course", "name", "file", "add_time"]
    search_fields = ["course", "name", "file"]
    list_filter = ["course", "name", "file", "add_time"]


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(CourseResource, CourseResourceAdmin)
