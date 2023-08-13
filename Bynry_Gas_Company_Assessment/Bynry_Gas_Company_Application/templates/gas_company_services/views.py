from django.shortcuts import render
from .models import ServiceRequest

def submit_request(request):
    if request.method == 'POST':
        # Handle form submission
        return render(request, 'gas_service/submit_request.html')

def track_request(request, request_id):
    request = ServiceRequest.objects.get(id=request_id)
    return render(request, 'gas_service/track_request.html', {'request': request})
