from django.shortcuts import render, redirect, get_object_or_404
from .models import ServiceDatabase
from .forms import ServiceRequest

def submit_request(request):
    print(request.method)
    if(request.method == 'POST'):
        request_form_data = ServiceRequest(request.POST, request.FILES)
        
        print(request_form_data.is_valid())
        print(request_form_data.errors)
        
        if(request_form_data.is_valid()):
            # If input to all the fields are valid.
            
            print("FORM DATA VALID !!!!!!")
            customer_name = request_form_data.cleaned_data['customer_name']
            request_type = request_form_data.cleaned_data['request_type']
            request_details = request_form_data.cleaned_data['request_details']
            attachment = request_form_data.cleaned_data['attachment']
            status = request_form_data.cleaned_data['status']
            submitted_at = request_form_data.cleaned_data['submitted_at']
            resolved_at = request_form_data.cleaned_data['resolved_at']
            
            registered_data = ServiceDatabase(customer_name = customer_name,
                                              request_type = request_type,
                                              request_details = request_details,
                                              attachment = attachment,
                                              status = status,
                                              submitted_at = submitted_at,
                                              resolved_at = resolved_at
                                              )
            
            registered_data.save()
            return redirect('success_request')
        else:
            # If form input to the fields are not valid, page will get refreshed.
            
            request_form_data = ServiceRequest()
    else:
        request_form_data = ServiceRequest()
    
    return render(request, 'gas_company_services/submit_customer_request.html', {'form': request_form_data})

def success_request(request):
    return render(request, 'gas_company_services/request_successfully_submitted.html')
    

def fetch_particular_request(request):
    requests = ServiceDatabase.objects.all()
    print(request.GET)
    if 'customer_name' in request.GET:
        customer_name = request.GET['customer_name']
                
        search_results = requests.filter(customer_name=customer_name)
        print(search_results)
        
    else:
        search_results = []

    return render(request, 'gas_company_services/track_customer_request.html', {'requests': requests, 'search_results': search_results})
    
    
def fetch_all_requests(request):
    if request.method == 'GET':
        all_requests = ServiceDatabase.objects.all()
        return render(request, 'gas_company_services/list_all_customer_requests.html', {'requests': all_requests})