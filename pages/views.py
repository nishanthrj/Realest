from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtors

def index(response):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:2]
	context = {
		'listings': listings
	}

	return render(response, 'pages/index.html', context)

def about(response):

	return render(response, 'pages/about.html')
