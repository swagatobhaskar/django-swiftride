from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# importing the Invoice model from services app
from services.models import Invoice

# importing get_template from loader
from django.template.loader import get_template

# import render_to_pdf from util.py
from .utils import render_to_pdf

# Creating our view, it is a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):

        # getting the invoice of the last reservation by user
        invoice = Invoice.objects.filter(user = request.user).order_by('reservation__booking_time').last()

        # getting the template
        pdf = render_to_pdf('invoice.html',{'invoice': invoice})

         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
