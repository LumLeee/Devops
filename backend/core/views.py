import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message

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

# API to list and create messages (Meeting requirements for GET + POST)
@csrf_exempt
def message_api(request):
    if request.method == 'GET':
        messages = Message.objects.all().order_by('-created_at')[:10]
        data = [{"name": m.name, "content": m.content, "date": m.created_at.strftime("%Y-%m-%d %H:%M:%S")} for m in messages]
        return JsonResponse(data, safe=False)
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = Message.objects.create(
                name=data.get('name', 'Anonymous'),
                content=data.get('content', '')
            )
            return JsonResponse({"status": "success", "id": message.id}, status=201)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)
