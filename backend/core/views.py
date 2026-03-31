from django.shortcuts import render
from django.http import JsonResponse
from .models import StudentProfile

def about(request):
    # Fetch all student profiles from Database to display a list
    students = StudentProfile.objects.all()
    
    context = {
        'students': students,
    }
    
    if not students:
        context['error_message'] = 'Không có dữ liệu trong Database.'
    
    # Get app name from settings/env
    import environ
    env = environ.Env()
    context['app_name'] = env('APP_NAME', default='Student Management System')
    
    return render(request, 'core/about.html', context)

def health_check(request):
    return JsonResponse({"status": "ok"})
