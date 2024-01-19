from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import BinEntry, BinHabit, NumEntry, NumHabit
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
            { "months": months, "title": "Habit One", "kind": "bin" },
            request))

def calendarNum(request, cal_id):
    template = loader.get_template("ht/calendar.html")
    months = getCal("num", cal_id)

    return HttpResponse(template.render(
            { "months": months, "title": "Habit One", "kind": "num" }, 
            request))

def calendarAll(request):
    template = loader.get_template("ht/calendar.html")
    months = getCal("all")

    return HttpResponse(template.render(
            { "months": months, "title": "All Calendars", "kind": "all" }, 
            request))

def summary(request, sum_id):
	return HttpResponse("summary %s" % sum_id)

def summaryAll(request):
	return HttpResponse("summary all")

#! ============================================================================
#! =============== MAKE THIS A MODULE AND NOT JUST CHILLIN HERE ===============
#! ============================================================================

def getCal(type: str, id: int = 0) -> dict:
    months = [0]*12

    for i in range(0,12):
        months[i] = makeCalItem(date(2024,i+1,1))

    ents = []

    if (type == "bin"):
        ents = BinEntry.objects.filter(habit=id)
        
        for ent in ents:
            months[ent.date.month-1]["days"][ent.date.day-1]['val']\
                = "success" if ent.res else "set back"

    if (type == "num"):
        ents = NumEntry.objects.filter(habit=id)    

        for ent in ents:
            months[ent.date.month-1]["days"][ent.date.day-1]['val']\
                = ent.res

    elif (type == "all"):
        size = len(BinHabit.objects.all()) + len(NumHabit.objects.all())
        ents = [*BinEntry.objects.all(),*NumEntry.objects.all()]    

        for ent in ents:
            if months[ent.date.month-1]["days"][ent.date.day-1]['val']\
                == None:
                    months[ent.date.month-1]["days"][ent.date.day-1]['val']\
                    = 1 / size
            else:
                 months[ent.date.month-1]["days"][ent.date.day-1]['val']\
                    = months[ent.date.month-1]["days"][ent.date.day-1]['val']\
                    + 1 / size
    
    print(ents)

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