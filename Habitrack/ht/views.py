from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import BinEntry, BinHabit, NumEntry, NumHabit
from datetime import date

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

def select(request):
    template = loader.get_template("ht/select.html")
    return HttpResponse(template.render({}, request))

def calendarBin(request, cal_id):
    template = loader.get_template("ht/calendar.html")
    months = getCal()

    thing = BinEntry.objects
    return HttpResponse(template.render(
            { "months": months, "title": "Habit One", "loaded": type(thing) },
            request))

def calendarNum(request, cal_id):
    template = loader.get_template("ht/calendar.html")
    months = getCal()
    return HttpResponse(template.render(
            { "months": months, "title": "Habit One" }, 
            request))

def calendarAll(request):
	return HttpResponse("calendar all")

def summary(request, sum_id):
	return HttpResponse("summary %s" % sum_id)

def summaryAll(request):
	return HttpResponse("summary all")

#! ============================================================================
#! =============== MAKE THIS A MODULE AND NOT JUST CHILLIN HERE ===============
#! ============================================================================

def getCal() -> dict:
    months = [0]*12

    for i in range(0,12):
        months[i] = makeCalItem(date(2024,i+1,1))
    return months

def makeCalItem(dat: date) -> dict:
    leng = getMonthLength(dat.month)
    dage = [{ "day": i, "val": None } for i in range(1,leng+1)]

    return {
        "month": getMonthName(dat.month),
        "num": leng,
        "days": dage,
        "offset": dat.weekday()
    }

def getMonthName(num: int) -> str:
    names = ["January", "February", "March", "April", "May", "June", "July", 
             "August", "September", "October", "November", "December"]
    return names[num - 1]

def getMonthLength(num: int) -> int:
    names = [31,29,31,30,31,30,31,31,30,31,30,31]
    return names[num - 1]