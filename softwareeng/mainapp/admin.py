from django.contrib import admin # type: ignore
from .models import Car, Football, Audio

admin.site.register(Car)
admin.site.register(Football)
admin.site.register(Audio)
