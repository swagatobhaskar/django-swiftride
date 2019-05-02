from django import forms
from .models import *
from django.contrib.auth.models import User
import datetime
# following mozilla examle
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class NewReservationForm(forms.ModelForm):
    class Meta:
        model= Reservation
        exclude = ['user','chosen_vehicle','garage','booking_time','city','area']
        # labels = {'garage': _('Where from: ')}
        help_texts = {'time_from': _('Enter your car picking time.'), 'time_to':_('Time you will return the car.')}
        widgets = {'date_from': forms.DateTimeInput(attrs={'class':'form-control datetimepicker-input', 'data-target': '#datetimepicker1'})}

    def clean_date_from(self):   # Syntax:  clean_<field_name>
        d_from = self.cleaned_data['date_from']      # This step gets us the data "cleaned" and sanitized of potentially
                                                    # unsafe input using the default validators, and converted into the
                                                    # correct standard type for the data (in this case a Python datetime.datetime object).
        # Check if a date is not in the past.
        if d_from < datetime.date.today():
            raise ValidationError(_('Invalid date - you are putting past date!'))
        return d_from

    def clean_date_to(self):
        to = self.cleaned_data['date_to']

        # Check if a date is not in the past.
        if to < datetime.date.today():
            raise ValidationError(_('Invalid date - you are putting past date!'))
        return to

"""
MOZILLA EXAMPLE
        def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data
"""

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        exclude = ['user']

class AddCardForm(forms.ModelForm):
    class Meta:
        model = Card_detail
        exclude = ['user']

    def clean_year_expires(self):
        year = self.cleaned_data['year_expires']
        if year < datetime.date.today():
            raise ValidationError(_('This card has already expired!'))
        return year

class AddLicenseForm(forms.ModelForm):
    class Meta:
        model = Driving_license
        exclude = ['user']
        help_texts = {'license_issued_in': _('Country/State'),}
        error_messages = {
            'license_issued_in': {
                'max_length': _("This is exceeding 20 characters."),
            },
        }
        # initial = {"field_name": "blahblah"}
        # initial=(instance = some_callable_modelobject)

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        if dob > datetime.date.today():
            raise ValidationError(_('Enter correct date of birth!'))
        return dob

    def clean_expiry_date(self):
        date = self.cleaned_data['expiry_date']
        if date < datetime.date.today():
            raise ValidationError(_('Enter correct date of expiry!'))
        return date
        
"""
NOW OBSOLETE

class GarageAndCategorySelectionForm(forms.Form):
    garage_from = forms.ModelChoiceField(queryset = Garage.objects.all(), label='Select the garage:', required = True)
    car_type = forms.ModelChoiceField(queryset = Category.objects.all(), label='Select the type of car:', required = True)
"""
