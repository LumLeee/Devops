from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

# Create your views here.

def about(request):
    # Using Django's global environment variables if set in settings, or direct from env
    # For now, let's just use django-environ logic indirectly
    import environ
    env = environ.Env()
    
    context = {
        'student_name': env('STUDENT_NAME', default='N/A'),
        'student_id': env('STUDENT_ID', default='N/A'),
        'student_class': env('STUDENT_CLASS', default='N/A'),
        'app_name': env('APP_NAME', default='Django App')
    }
    return render(request, 'core/about.html', context)

def health_check(request):
    return JsonResponse({"status": "ok"})
