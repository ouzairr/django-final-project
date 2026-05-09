from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Question, Submission, Choice

# Task 5: submit and show_exam_result functions
def submit(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, pk=course_id)
        # Logic to gather selected choices from the POST request
        # and create a Submission object would go here
        return redirect('onlinecourse:show_exam_result', course_id=course.id)

def show_exam_result(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # Logic to calculate the score and pass it to the template
    context = {'course': course}
    return render(request, 'onlinecourse/exam_result.html', context)