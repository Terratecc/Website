from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from .forms import *

# Create your views here.

def homepage(request):
	context = {}
	if request.method == "POST":
		form = ContactForm(request.POST)
		context = {'form': form}
		if form.is_valid():
			clean_form = form.cleaned_data
			# send the email to the recipent
			send_mail('Terratecc Alert: ' + clean_form['subject'], clean_form['name'] + ' - ' + clean_form['email'] + '\n' + clean_form['budget'] + '\n' +  clean_form['message'], settings.DEFAULT_FROM_EMAIL, ['info@terratecc.com'])
			send_mail('Terratecc', 'Your message has been sent!' + '\n' + 'Our team will get back to you as soon as possible.' + '\n' + '\n' + 'Cheers,' + '\n' + 'The Terratecc Team', settings.DEFAULT_FROM_EMAIL, [clean_form['email']])
			return redirect('/sent')

	template = loader.get_template('main/index.html')
	return HttpResponse(template.render(context, request))

def error404(request, slug):
	context = {}
	template = loader.get_template('main/error404.html')
	return HttpResponse(template.render(context, request))

def messageSent(request):
	context = {}
	template = loader.get_template('main/message_sent.html')
	return HttpResponse(template.render(context, request))


