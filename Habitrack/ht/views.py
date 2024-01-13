from django.http import HttpResponse

# Let's start  this from the top, shall we? When I start  the app, I want it to 
# generate a list of binary and numeric habits. I think that the easiest way to
# do  this would simply be to  currently have  it query all binary and  numeric 
# tasks.  Then I could make a  couple different pages. I  think there will be a 
# calendar  page, a  summary page, and each of  these will have the  ability to 
# have  an  individual habit selected  or to select  all habits. This  gives us 
# routes for /summary/<id>, /summary/all, /calendar/<id>, and /calendar/all. 

def index(request):
	return HttpResponse("Hello butt")
