from django.http import HttpResponse, JsonResponse

# Let's start  this from the top, shall we? When I start  the app, I want it to 
# generate a list of binary and numeric habits. I think that the easiest way to
# do  this would simply be to  currently have  it query all binary and  numeric 
# tasks.  Then I could make a  couple different pages. I  think there will be a 
# calendar  page, a  summary page, and each of  these will have the  ability to 
# have  an  individual habit selected  or to select  all habits. This  gives us 
# routes for /summary/<id>, /summary/all, /calendar/<id>, and /calendar/all. 

def index(request):
	return HttpResponse("Hello butt")

def calendar(request, cal_id):
	return HttpResponse("calendar %s" % cal_id)

def calendarAll(request):
	return HttpResponse("calendar all")

def summary(request, sum_id):
	return HttpResponse("summary %s" % sum_id)

def summaryAll(request):
	return HttpResponse("summary all")
