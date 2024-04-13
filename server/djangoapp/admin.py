from django.contrib import admin
from .models import CarMake, CarModel, Dealership

# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Dealership)
