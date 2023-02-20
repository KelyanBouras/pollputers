from django.contrib import admin
from .models import *

# Register the models for the admin panel.
admin.site.register(Brand)
admin.site.register(OS)
admin.site.register(Processor)
admin.site.register(OSChoice)

