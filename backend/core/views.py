import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# About page (as per requirement)
def about(request):
    import environ
    env = environ.Env()
    context = {
        'student_name': env('STUDENT_NAME', default='Guest User'),
        'student_id': env('STUDENT_ID', default='SV_UNKNOWN'),
        'student_class': env('STUDENT_CLASS', default='Class_UNKNOWN'),
        'app_name': env('APP_NAME', default='Student App')
    }
    return render(request, 'core/about.html', context)

# Health check
def health_check(request):
    return JsonResponse({"status": "ok"})
