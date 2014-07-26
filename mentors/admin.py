from django.contrib import admin

from .models import Mentor, Industry, Degree, Company

# Register your models here.
admin.site.register(Mentor)
admin.site.register(Industry)
admin.site.register(Degree)
admin.site.register(Company)