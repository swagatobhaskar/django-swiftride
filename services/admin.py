from django.contrib import admin
from .models import *

class Car_modelAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'category')

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id','car_no','car_model', 'garage')

class GarageAdmin(admin.ModelAdmin):
    list_display = ('name','street')

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id','area_name','city')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Garage, GarageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Car_model, Car_modelAdmin) # notice this 2nd parameter
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Account)
admin.site.register(Reservation)
admin.site.register(Driving_license)
admin.site.register(Driving_plan)
admin.site.register(Card_detail)
admin.site.register(Payment_receipt)
admin.site.register(Area, AreaAdmin)
admin.site.register(City)
admin.site.register(Invoice)
