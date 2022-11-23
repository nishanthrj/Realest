from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact(request):
	if request.method == "POST":
		listing = request.POST['listing']
		listing_id = request.POST['listing_id']
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		user_id = request.POST['user_id']
		realtor_email = request.POST['realtor_email']

		if request.user.is_authenticated:
			user_id = request.user.id
			has_contacted = Contact.objects.all().filter(user_id=user_id, listing_id=listing_id)
			if has_contacted:
				messages.error(request, "You have already made an Inquiry for this property.")
				return redirect('/listings/' + listing_id)

		contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
		contact.save()

		messages.success(request, "Your request has been submitted. A Realtor will reach out to you soon")
		return redirect('/listings/' + listing_id)
