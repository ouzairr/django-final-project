from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Submission, Choice, Enrollment

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        enrollment = get_object_or_404(Enrollment, user=request.user, course=course)
        submission = Submission(enrollment=enrollment)
        submission.save()
        
        selected_ids = request.POST.getlist('choice')
        for choice_id in selected_ids:
            choice = get_object_or_404(Choice, pk=choice_id)
            submission.choices.add(choice)
        submission.save()
        
        return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=submission.id)

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    selected_ids = submission.choices.values_list('id', flat=True)
    
    total_score = 0
    earned_score = 0
    results = []
    
    for question in course.lesson_set.all().values_list('question', flat=True):
        pass

    # Calculate score through lessons
    for lesson in course.lesson_set.all():
        for question in lesson.question_set.all():
            total_score += question.grade
            if question.is_get_score(selected_ids):
                earned_score += question.grade
            results.append({
                'question': question,
                'correct': question.is_get_score(selected_ids)
            })
    
    percentage = round((earned_score / total_score * 100), 1) if total_score > 0 else 0
    passed = percentage >= 70

    context = {
        'course': course,
        'submission': submission,
        'score': percentage,
        'earned_score': earned_score,
        'total_score': total_score,
        'results': results,
        'passed': passed,
    }
    return render(request, 'onlinecourse/exam_result.html', context)
def index(request):
    courses = Course.objects.all()
    return render(request, 'onlinecourse/course_list.html', {'courses': courses})
def exam(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lesson_set.all()
    return render(request, 'onlinecourse/exam.html', {
        'course': course,
        'lessons': lessons
    })  
