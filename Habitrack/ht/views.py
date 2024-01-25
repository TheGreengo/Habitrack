from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import BinEntry, BinHabit, NumEntry, NumHabit
from .utils import getCal
from datetime import date

def index(request):
	return HttpResponse("Hello butt")

def select(request):
    template = loader.get_template("ht/select.html")

    bins = BinHabit.objects.all()
    nums = NumHabit.objects.all()

    stuff = []

    for bin in bins:
         stuff.append({"name":bin.name,"id":bin.id, "type": "bin" })
    for num in nums:
         stuff.append({"name":num.name, "id":num.id, "type": "num"})

    return HttpResponse(template.render({ "things": stuff }, request))

def calendarBin(request, cal_id):
    template = loader.get_template("ht/calendar.html")
    months = getCal("bin", cal_id)

    return HttpResponse(template.render(
            { "months": months, "title": "Habit One", "kind": "bin", "id": cal_id },
            request))

def calendarNum(request, cal_id):
    template = loader.get_template("ht/calendar.html")
    months = getCal("num", cal_id)

    return HttpResponse(template.render(
        { "months": months, "title": "Habit One", "kind": "num", "id": cal_id }, 
        request))

def calendarAll(request):
    template = loader.get_template("ht/calendar.html")
    months = getCal("all")

    return HttpResponse(template.render(
            { "months": months, "title": "All Calendars", "kind": "all" }, 
            request))

#* link opens up a update entry page for a certain date
#* we then need a for that page to have a form to update or create a new
#* entry for that date. Once that is submitted, it then needs to redirect
#* to the appropriate calendar page

def binSubmit():
    print("Hello")

def numSubmit():
    print("Hello")

def updateBin(request, cal_id, dat):
    template = loader.get_template("ht/update.html")
    day = date(2024, dat // 100, dat % 100)

    return HttpResponse(template.render(
        {"date": day, "kind": "bin", "id": cal_id }, 
        request))


def updateNum(request, cal_id, dat):
    template = loader.get_template("ht/update.html")
    day = date(2024, dat // 100, dat % 100)

    return HttpResponse(template.render(
        {"date": day, "kind": "num", "id": cal_id }, 
        request))

def summary(request, sum_id):
	return HttpResponse("summary %s" % sum_id)

def summaryAll(request):
	return HttpResponse("summary all")