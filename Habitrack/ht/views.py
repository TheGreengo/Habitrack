from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import BinEntry, BinHabit, NumEntry, NumHabit
from django.views.decorators.csrf import csrf_protect
from .utils import getCal, getNumDate
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
    name = BinHabit.objects.filter(id=cal_id)[0].name

    return HttpResponse(template.render(
            { "months": months, "title": name, "kind": "bin", "id": cal_id },
            request))

def calendarNum(request, cal_id):
    template = loader.get_template("ht/calendar.html")
    months = getCal("num", cal_id)
    name = NumHabit.objects.filter(id=cal_id)[0].name

    return HttpResponse(template.render(
        { "months": months, "title": name, "kind": "num", "id": cal_id }, 
        request))

def calendarAll(request):
    template = loader.get_template("ht/calendar.html")
    months = getCal("all")

    return HttpResponse(template.render(
            { "months": months, "title": "All Calendars", "kind": "all" }, 
            request))

@csrf_protect
def submitBin(request, cal_id):

    val = not (request.POST.get("res") == None)
    print(val)
    habit = BinHabit.objects.filter(id = cal_id)
    dat = date(*getNumDate(request.POST.get("date")))
    ent = BinEntry(habit=habit[0], 
                   res=val, 
                   date=dat)
    ent.save()

    response = redirect(f'/calendar/bin/{cal_id}/')
    return response

@csrf_protect
def submitNum(request, cal_id):

    habit = NumHabit.objects.filter(id = cal_id)

    dat = date(*getNumDate(request.POST.get("date")))
    num = float(request.POST.get("res"))
    ent = NumEntry(habit=habit[0], 
                   res=num, 
                   date=dat)
    ent.save()

    response = redirect(f'/calendar/num/{cal_id}/')
    return response

@csrf_protect
def updateBin(request, cal_id, dat):
    template = loader.get_template("ht/update.html")
    mon = str((dat // 100)) if (dat // 100) >= 10 else "0" + str((dat // 100))
    dag = str((dat % 100)) if (dat % 100) >= 10 else "0" + str((dat % 100))
    day = f"2024-{mon}-{dag}"

    return HttpResponse(template.render(
        {"date": day, "kind": "bin", "id": cal_id, "dat":dat }, 
        request))

@csrf_protect
def updateNum(request, cal_id, dat):
    template = loader.get_template("ht/update.html")
    mon = str((dat // 100)) if (dat // 100) >= 10 else "0" + str((dat // 100))
    dag = str((dat % 100)) if (dat % 100) >= 10 else "0" + str((dat % 100))
    day = f"2024-{mon}-{dag}"

    return HttpResponse(template.render(
        {"date": day, "kind": "num", "id": cal_id, "dat":dat }, 
        request))

def summary(request, sum_id):
	return HttpResponse("summary %s" % sum_id)

def summaryAll(request):
    template = loader.get_template("ht/summary.html")

    bins = BinHabit.objects.all()
    nums = NumHabit.objects.all()

    things = []

    for i in bins:
        ents = BinEntry.objects.filter()
        thing = {
            "type": "bin",
            "name": i.name,
            "goal": i.goal
        }
        things.append(thing)
        
        
    # basically we want to make a list of habit objects, where each habit object 
    # has the name of the habit (easy), the goal of the habit (easy), the 
    # current rate of success/status, a list of the values, the days needed for 
    # to meet the goal, days in, days left, 
    # Since this 
    thing = {
        "vals": [0,1,0,1],
        "curr": 0.7,
        "days in": 3,
        "days to go": 6,
        "days needed": 4,
        "other": "thing"
    }
    return HttpResponse(template.render({ "things": "thang" }, request))