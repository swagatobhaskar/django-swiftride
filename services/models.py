from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class City(models.Model):
    city_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.city_name

class Area(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    area_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.area_name

class Garage(models.Model):
    name = models.CharField (max_length = 30, blank=False)
    zip = models.IntegerField (blank=True, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    street = models.CharField(max_length=20, blank=True)
    pic = models.ImageField (upload_to ='images/garages')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField (max_length = 15, blank=False)
    photo = models.ImageField(upload_to = 'images/car_categories', null=True)

    def __str__(self):
        return self.name

class Car_model(models.Model):
    name = models.CharField (max_length = 25, blank=False)
    company = models.CharField (max_length = 15, blank=False)
    mileage = models.DecimalField (max_digits=4, decimal_places=1, blank=False)
    rent_per_hour = models.DecimalField (max_digits=6, decimal_places=4, blank=False)
    category = models.ForeignKey (Category, on_delete=models.CASCADE)
    photo = models.ImageField (upload_to ='images/models')
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    car_no = models.CharField (max_length = 20, blank=False)
    car_model = models.ForeignKey (Car_model, on_delete=models.CASCADE)
    garage = models.ForeignKey (Garage, on_delete=models.CASCADE)
    available = models.BooleanField(default = True)
    def __str__(self):
        return "Car no: "+self.car_no
    class Meta:
        ordering = ['id']

class Account(models.Model):   # Extending the User model to create profile.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField (upload_to ='images/profile-photos', verbose_name="Upload a profile picture")
    mobile = models.IntegerField(blank=False)
    city = models.CharField (max_length = 20, blank=False)
    building_no = models.CharField (max_length = 15, blank=False)
    state = models.CharField (max_length = 15, blank=False)
    zip = models.IntegerField (blank=False)
    country = models.CharField (max_length = 20, blank=False)
    sex = models.CharField (max_length=12, blank=True)

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_from = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    date_to = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    time_from = models.TimeField(auto_now=False, auto_now_add=False, blank=False)
    time_to = models.TimeField(auto_now=False, auto_now_add=False, blank=False)
    destination=models.CharField(max_length=20, blank=False, verbose_name="Where will you go")
    chosen_vehicle=models.CharField(max_length = 20, blank=False, default='')
    booking_time=models.DateTimeField(default = datetime.now)
    garage = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20, default='')
    area = models.CharField(max_length = 20, default='')

    def __str__(self):
        return "Booked by: "+self.user.username +" "+self.chosen_vehicle

class Driving_license(models.Model):
    license_issued_in = models.CharField (max_length = 20, blank=False)   # in country and state as one char.  separated by a /
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    license_no = models.CharField (max_length=15, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expiry_date = models.DateField(auto_now=False, auto_now_add=False, blank=False)

    def __str__(self):
        return self.user.first_name+" "+self.license_no

class Driving_plan(models.Model):
    plan = models.CharField (max_length=25, blank=False)
    duration = models.CharField(max_length=15)
    details1 = models.TextField(blank=True)
    details2 = models.TextField(blank=True)
    one_time_fee = models.DecimalField(max_digits=4, decimal_places=2, default=25.00)
    hourly_rate = models.DecimalField(max_digits=4, decimal_places=2, default=08.00)
    monthly_rate = models.DecimalField(max_digits=4, decimal_places=2, default=00.00)
    daily_rate = models.DecimalField(max_digits=4, decimal_places=2, default=65.00)
    annual_fee = models.DecimalField(max_digits=4, decimal_places=2, default=50.00)
    def __str__(self):
        return self.plan

class Card_detail(models.Model):
    card_no = models.IntegerField()
    year_expires = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    cardholder_name = models.CharField (max_length=30, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Payment_receipt(models.Model):
    driving_plans = models.ForeignKey(Driving_plan, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.driving_plans.plan+"  --  "+self.user.first_name+" "+self.user.last_name

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "Invoice of: "+ self.user.first_name+" "+self.user.last_name+"  |  "+"Reservation id: "+str(self.reservation.id)
