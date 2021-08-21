from django.contrib import admin
from main import models
from django.contrib import admin
from .models import *
admin.site.register(Car)
admin.site.register(PositionCategory)
admin.site.register(Credit)
admin.site.register(Payment)


