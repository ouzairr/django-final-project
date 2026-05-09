from django.contrib import admin
from .models import Course, Lesson, Instructor, Question, Choice

# Task 2: QuestionInline, ChoiceInline, QuestionAdmin, and LessonAdmin
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Register classes
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)