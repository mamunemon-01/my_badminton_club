#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

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
	template = loader.get_template("template.html")
	context = {
		#"fruits": ['Dates', 'Guava', 'Jackfruit']
		'firstname': 'Mamun'
	}
	return HttpResponse(template.render(context, request))