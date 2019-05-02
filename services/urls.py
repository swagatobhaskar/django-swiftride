from django.urls import path
from . import views

# ALL URLS START WITH 'SERVICES'

urlpatterns=[
    path('all/', views.servicesview, name='services'),
    path('review/', views.reviewView, name='review'),
    path('carmodels/', views.carmodelsView, name='all_car_models'),
    path('profilecomplete/', views.profilecompleteView, name='profile_complete'),
    path('getting-started/', views.gettingstartedView, name='getting_started'),

    # city and area select pages
    path('availablecities/', views.cityselectView, name='select_city'),
    path('selectarea/<str:city_name>/', views.areaselectView, name='select_area'),
    path('selectgarage/<str:area_name>/', views.garageselectView, name='select_garage'),
    path('availabletypes/<str:name>/', views.carcategoryView, name='select_car_category'),
    path('selectmodel/<str:name>/<str:type>/', views.modelselectView, name='select_model'),
    path('allocate.vehicle/<str:model_name>/<str:garage_name>/', views.carAllocateView ,name='allocate_car'),

    # reservation pages:
    path('newbooking/<int:pk>/', views.NewBookingView, name='booking'),
    path('bookingsuccessful/<int:pk>/', views.successpageView, name='success_page'),

    # invoice showing and printing page
    path('bookinginvoice/<int:pk>/', views.invoiceView, name='invoice'),

    # profile viewing and editing pages:
    path('addprofile/', views.addprofileView, name='add_user_profile'),
    path('profile/', views.ProfileView, name='view_profile'),
    path('profile/edit/<int:pk>/', views.editprofileView, name='edit_profile'),

    # reservation history page
    path('reservationhistory/', views.bookingrecordsView, name='booking_history'),

    # plan viewing and editing pages:
    path('drivingplans/', views.plansView, name='plans'),
    path('selectplan/', views.planselectView, name='plan_select'),
    path('planselected/<int:pk>/', views.passPlanPKView, name='selected_plan'),
    path('purchasedplan/', views.showselectedplanView, name='show_selected_plan'),

    # Driving license viewing and editing pages:
    path('addlicense/', views.addlicenseView, name='add_license'),
    path('viewlicense/', views.savedlicenseView, name='saved_license'),
    path('editlicense/<int:pk>/', views.editsavedlicenseView, name='edit_license'),

    #Credit/debit card viewing and editing pages:
    path('addcard/', views.addcardView, name='add_card'),
    path('savedcard/', views.savedcardView, name='show_saved_card'),
    path('updatecard/<int:pk>/', views.updatecardView ,name='edit_card'),
]
