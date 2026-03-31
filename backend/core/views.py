from django.shortcuts import render
from django.http import JsonResponse
from .models import StudentProfile

def about(request):
    # Fetch student profile from Database instead of environment variables
    # We'll take the first student in the table for reference
    student = StudentProfile.objects.first()
    
    if student:
        context = {
            'student_name': student.fullname,
            'student_id': student.student_id,
            'student_class': student.class_name,
        }
    else:
        # Fallback if DB is empty
        context = {
            'student_name': 'No data in DB',
            'student_id': 'N/A',
            'student_class': 'N/A',
        }
    
    # Optionally get app name from settings/env as it's a configuration
    import environ
    env = environ.Env()
    context['app_name'] = env('APP_NAME', default='Student App')
    
    return render(request, 'core/about.html', context)

def health_check(request):
    return JsonResponse({"status": "ok"})
