from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import BinEntry, BinHabit, NumEntry, NumHabit

# Let's start  this from the top, shall we? When I start  the app, I want it to 
# generate a list of binary and numeric habits. I think that the easiest way to
# do  this would simply be to  currently have  it query all binary and  numeric 
# tasks.  Then I could make a  couple different pages. I  think there will be a 
# calendar  page, a  summary page, and each of  these will have the  ability to 
# have  an  individual habit selected  or to select  all habits. This  gives us 
# routes for /summary/<id>, /summary/all, /calendar/<id>, and /calendar/all.
# The all calendar just shows how many of the habits were logged that day. 
# Which brings us to the calendar situation... we need a month class, with a 
# list of day classes, each day needs to only have a number (the date) and a 
# value, which can either be a number or a boolean

def index(request):
	return HttpResponse("Hello butt")

def calendar(request, cal_id):
    template = loader.get_template("ht/calendar.html")
    return HttpResponse(template.render({"thing":cal_id}, request))

def calendarAll(request):
	return HttpResponse("calendar all")

def summary(request, sum_id):
	return HttpResponse("summary %s" % sum_id)

def summaryAll(request):
	return HttpResponse("summary all")
