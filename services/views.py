from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewReservationForm, UserProfileForm, AddCardForm, AddLicenseForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
import datetime
from datetime import timedelta
#  ----- basic views -----

def homeview(request):
    if request.user.is_authenticated:
        if not Payment_receipt.objects.filter(user = request.user).exists():
            return redirect('plan_select')
        if not Account.objects.filter(user = request.user).exists():
            return redirect('add_user_profile')
        if not Driving_license.objects.filter(user = request.user).exists():
            return redirect('add_license')
        if not Card_detail.objects.filter(user = request.user).exists():
            return redirect('add_card')
    return render(request, 'services/home.html')

def aboutview(request):
    return render(request, 'services/about.html')

def servicesview(request):
    return render(request, 'services/services.html')

def carmodelsView(request):
    mod = Car_model.objects.all()
    return render(request, 'services/carmodels.html', {'mod': mod})

def reviewView(request):
    return render(request, 'services/reviewpage.html')

def gettingstartedView(request):
    return render(request, 'services/getting-started-page.html')

# ------ add/edit profile views ---------

@login_required
def addprofileView(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_user_profile = form.save(commit=False)
            new_user_profile.user = request.user
            new_user_profile.save()
            return redirect('add_license')
    else:
        form = UserProfileForm()
    return render(request, 'services/addprofile.html', {'form': form})

@login_required
def ProfileView(request):
    user = request.user
    profile = Account.objects.filter(user = user)
    return render(request, 'services/userprofile.html', {'pr': profile})

@login_required
def editprofileView(request, pk):
    ac = get_object_or_404(Account, pk=pk)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=ac)
        if form.is_valid():
            ac = form.save(commit=False)
            ac.user = request.user
            ac.save()
            return redirect('view_profile')
    else:
        form=UserProfileForm(instance=ac)
    return render(request, 'services/addprofile.html', {'form': form})

def profilecompleteView(request):   # shows after adding plan->profile->license->card
    return render(request, 'services/profilecompletepage.html')

# ------- add/edit card views --------

@login_required
def addcardView(request):
    if request.method == "POST":
        form = AddCardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.save()
            return redirect('profile_complete')
    else:
        form = AddCardForm()
    return render(request, 'services/addcard.html', {'form': form})

@login_required
def savedcardView(request):
    user = request.user
    cards = Card_detail.objects.filter(user = user)
    return render(request, 'services/saved_card_display_page.html', {'card': cards})

@login_required
def updatecardView(request, pk):
    card = get_object_or_404(Card_detail, pk = pk)
    if request.method =="POST":
        form = AddCardForm(request.POST, instance=card)
        if form.is_valid():
            card = form.save(commit=False)
            card.user=request.user
            card.save()
            return redirect('show_saved_card')
    else:
        form = AddCardForm(instance = card)
    return render(request, 'services/addcard.html', {'form': form})

# --- add/edit Driving license views -------

@login_required
def addlicenseView(request):
    if request.method == "POST":
        form = AddLicenseForm(request.POST)
        if form.is_valid():
            license=form.save(commit=False)
            license.user=request.user
            license.save()
            return redirect('add_card')
    else:
        form = AddLicenseForm()
    return render(request, 'services/addlicense.html', {'form': form})

@login_required
def savedlicenseView(request):
    user = request.user
    license = Driving_license.objects.filter(user = user)
    return render(request, 'services/view_saved_license.html', {'lcn': license})

@login_required
def editsavedlicenseView(request, pk):
    dli = get_object_or_404(Driving_license, pk=pk)
    if request.method =="POST":
        form = AddLicenseForm(request.POST, instance = dli)
        if form.is_valid():
            dli = form.save(commit=False)
            dli.user = request.user
            dli.save()
            return redirect('saved_license')
    else:
        form = AddLicenseForm(instance = dli)
    return render(request, 'services/addlicense.html', {'form': form})

# ---- driving plan views ------

def plansView(request):
    plan = Driving_plan.objects.all()
    return render(request, 'services/planspage.html', {'plans': plan})

@login_required
def planselectView(request):
    plans = Driving_plan.objects.all()
    return render(request, 'services/planselectpage.html', {'plan': plans})

def calcEnddate(plan):
    start_date = datetime.date.today()
    if plan.id == 1:
        end_date = start_date + datetime.timedelta(days = 365)
    elif plan.id == 2:
        end_date = start_date + datetime.timedelta(days = 365)
    else:
        end_date = start_date + datetime.timedelta(days = 365)
    return end_date

@login_required
def passPlanPKView(request, pk):
    plan = Driving_plan.objects.get(pk = pk)
    Pay = Payment_receipt.objects.create(
        driving_plans=plan,
        user = request.user,
        start_date=datetime.date.today(),
        end_date= calcEnddate(plan),
    )
    return redirect('add_user_profile')

@login_required
def showselectedplanView(request):
    user = request.user
    purchased_by = Payment_receipt.objects.filter(user = user)
    return render(request, 'services/purchased_plan_page.html', {'by': purchased_by})

# -------- City -> Area -> Vehicle_category -> Vehicle_model -> Vehicle select views ---------

def cityselectView(request):
    cities = City.objects.all()
    return render(request, 'services/city_select_page.html', {'cities': cities})

def areaselectView(request, city_name):
    areas = Area.objects.filter(city__city_name = city_name)
    return render(request, 'services/area_select_page.html', {'areas': areas})

def garageselectView(request, area_name):
    garages = Garage.objects.filter(area__area_name = area_name)
    return render(request, 'services/garage_select_page.html', {'garages': garages})

def carcategoryView(request, name):
    garage_name = Garage.objects.get(name = name)
    type = Category.objects.all()
    return render(request, 'services/car_type_select_page.html', {'type': type, 'garage': garage_name})

def modelselectView(request, name, type):
    try:
        g = Garage.objects.get(name = name)
        models = Car_model.objects.filter(vehicle__garage__name= name).filter(category__name = type).distinct()
    except Car_model.DoesNotExist:
        raise Http404
    return render(request, 'services/car_model_select_page.html', {'models': models, 'g': g})

def carAllocateView(request, model_name, garage_name):
    v = Vehicle.objects.filter(garage__name = garage_name).filter(car_model__name = model_name).order_by('id').first()
    return redirect('booking', v.id)

# --- Booking history and invoice view ----

@login_required
def bookingrecordsView(request):
    rsv = Reservation.objects.filter(user = request.user)
    return render(request, 'services/booking_history_page.html', {'rsv': rsv})

@login_required
def invoiceView(request, pk):
    # get the reservation instance
    present_reservation = Reservation.objects.get(pk = pk)
    # get the reserved car
    reserved_car = present_reservation.chosen_vehicle
    # pass the reserved car to the vehicle model
    r_car = Vehicle.objects.get(car_no = reserved_car)
    # get the Reservation fields
    start_date = present_reservation.date_from
    start_time = present_reservation.time_from
    end_date = present_reservation.date_to
    end_time = present_reservation.time_to
    # combine date and time fields into datetime
    start_datetime = datetime.datetime.combine(start_date, start_time)
    end_datetime = datetime.datetime.combine(end_date, end_time)
    # get the interval time
    interval = end_datetime - start_datetime
    # the interval time in seconds using timedelta.total_seconds()
    interval_in_s = interval.total_seconds()
    # converting seconds to hours
    hours = divmod(interval_in_s, 3600)[0]
    # get the hourly rent of the car model
    hourly_rent = r_car.car_model.rent_per_hour
    # calculate the cost
    cost = hours * float(hourly_rent)

    Invoice.objects.create(
        user = request.user, reservation = present_reservation,
        vehicle = r_car, hours = hours, cost = cost,
    )

    # pass data to template through context
    context = {
        'hours': hours, 'prsv': present_reservation, 'cost': cost, 'rcar': r_car,
    }
    return render(request, 'services/invoice_page.html', context=context)

#  --- booking views -----

@login_required
def NewBookingView(request, pk):
    v = Vehicle.objects.get(id = pk)
    if request.method == "POST":
        form = NewReservationForm(request.POST)
        if form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.user = request.user
            new_booking.chosen_vehicle = v.car_no
            new_booking.garage = v.garage
            new_booking.area = v.garage.area
            new_booking.city = v.garage.area.city
            new_booking.save()
            return redirect('success_page', new_booking.pk)
    else:
        form = NewReservationForm()
    return render(request, 'services/newbookingpage.html', {'form': form})

@login_required
def successpageView(request, pk):
    reserved = Reservation.objects.filter(id = pk)
    return render(request, 'services/success_page.html', {'reserved': reserved})

# ----- car available/unavailable views -----

"""
def carDBconfigView(request, pk):

"""
