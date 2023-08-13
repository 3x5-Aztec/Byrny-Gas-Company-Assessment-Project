from django.db import models
from datetime import datetime

class ServiceDatabase(models.Model):
    
    # current date and time
    now = datetime.now() 
    
    TYPES = (
        ('Gas Leak', 'Gas Leak'),
        ('Meter Reading', 'Meter Reading'),
        ('Physical Damage', 'Physical Damage'),
        ('Other', 'Other')
        # Add more types
    )
    
    customer_name = models.CharField(max_length = 100)
    request_type = models.CharField(max_length = 20, choices = TYPES)
    request_details = models.TextField()
    attachment = models.FileField(upload_to = 'attachments/')
    status = models.CharField(max_length = 20, default = 'Pending')
    
    submitted_at = models.CharField(max_length = 20, default = now.strftime("%m/%d/%Y, %H:%M:%S"))
    resolved_at = models.DateTimeField(null = True, blank = True)
    
    def __str__(self):
        return self.customer_name