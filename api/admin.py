from django.contrib import admin

from .models import Vaccination, Drug

admin.site.register(Vaccination)
admin.site.register(Drug)
