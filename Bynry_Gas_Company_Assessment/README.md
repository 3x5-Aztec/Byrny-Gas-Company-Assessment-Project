# Byrny-Gas-Company-Assessment-Project
This is a sample Python Django project for imitating a gas company which handles customer requests.
Don't forget to fill all the given fields because the form doesn't get submitted without it. Also make sure to click apply button when filling date fields.

The structure of a Django project typically follows a specific layout to maintain clarity, organization, and modularity. Here's a structure for a Byrny-Gas-Company-Assessment-Project Django application:


Byrny-Gas-Company-Assessment-Project/
└── Bynry_Gas_Company_Assessment/
       ├── manage.py
       ├── project_name/  
       │   ├── __init__.py
       │   ├── asgi.py
       │   ├── settings.py
       │   ├── urls.py
       |   ├── wsgi.py
       │   └── templates
       |          └── gas_company_services
       |                  ├── list_all_customer_requests.html
       |                  ├── request_successfully_submitted.html
       |                  └── submit_customer_request.html
       ├── Bynry_Gas_Company_Application/
       │   ├── migrations/
       │   │   ├── __init__.py
       │   │   ├── __pycache__/
       |   |            └── ...
       │   │   └── ...
       │   ├── __init__.py
       │   ├── admin.py
       │   ├── apps.py
       │   ├── models.py
       │   ├── tests.py
       │   ├── urls.py
       │   ├── forms.py
       │   └── views.py
       └── media/
              └── attachments/
                      └── ...
