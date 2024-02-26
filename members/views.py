#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

# Create your views here.
def members(request):
    #return HttpResponse("Hello World")
    the_members = Member.objects.all().values() # the QuerySet
    template = loader.get_template('all_members.html')
    context = {
    	'the_members': the_members
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
	the_member = Member.objects.get(id = id)
	template = loader.get_template("details.html")
	context = {
		"the_member": the_member
	}
	return HttpResponse(template.render(context, request))

def main(request):
	template = loader.get_template("main.html")
	return HttpResponse(template.render())

def testing(request):
	the_data = Member.objects.all().order_by('lastname', '-id').values()
	template = loader.get_template("template.html")
	context = {
		'the_members': the_data
	}
	return HttpResponse(template.render(context, request))