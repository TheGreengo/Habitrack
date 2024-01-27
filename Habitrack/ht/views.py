from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import BinEntry, BinHabit, NumEntry, NumHabit
from .forms import UpdateNumForm, UpdateBinForm
from django.views.decorators.csrf import csrf_protect
from .utils import getCal
from datetime import date
from django.shortcuts import redirect

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

#* what we have left to do is to add in:
#* - updating the objects in the DB

@csrf_protect
def submitBin(request, cal_id, dat):

    # habit = BinHabit.objects.filter(id = cal_id)
    # dat = date()
    # ent = BinEntry(habit=habit, res=, date=dat)
    form = UpdateBinForm(request.POST)
    print(form["date"].value())
    print(form["res"].value())

    response = redirect(f'/calendar/bin/{cal_id}/')
    return response

@csrf_protect
def submitNum(request, cal_id, dat):

    form = UpdateNumForm(request.POST)
    print(form["date"].value())
    print(form["res"].value())

    response = redirect(f'/calendar/num/{cal_id}/')
    return response

@csrf_protect
def updateBin(request, cal_id, dat):
    template = loader.get_template("ht/update.html")
    mon = str((dat // 100)) if (dat // 100) >= 10 else "0" + str((dat // 100))
    day = f"2024-{mon}-{dat % 100}"

    return HttpResponse(template.render(
        {"date": day, "kind": "bin", "id": cal_id, "dat":dat }, 
        request))

@csrf_protect
def updateNum(request, cal_id, dat):
    template = loader.get_template("ht/update.html")
    mon = str((dat // 100)) if (dat // 100) >= 10 else "0" + str((dat // 100))
    day = f"2024-{mon}-{dat % 100}"

    return HttpResponse(template.render(
        {"date": day, "kind": "num", "id": cal_id, "dat":dat }, 
        request))

def summary(request, sum_id):
	return HttpResponse("summary %s" % sum_id)

def summaryAll(request):
	return HttpResponse("summary all")