from .models import BinEntry, BinHabit, NumEntry, NumHabit
from datetime import date

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
            == None or \
            months[ent.date.month-1]["days"][ent.date.day-1]['val'] == "late":
                months[ent.date.month-1]["days"][ent.date.day-1]['val']\
                = 1 / size
            else:
                months[ent.date.month-1]["days"][ent.date.day-1]['val']\
                = months[ent.date.month-1]["days"][ent.date.day-1]['val']\
                + 1 / size

    return months

def makeCalItem(dat: date) -> dict:
    leng = getMonthLength(dat.month)
    curr = date.today()
    dage = []
    
    if dat.month < curr.month:
        dage = [{ "day": i, "val": "late" } for i in range(1,leng+1)]
    elif dat.month == curr.month:
        one = [{ "day": i, "val": "late" } for i in range(1,curr.day)]
        two = [{ "day": i, "val": None } for i in range(curr.day,leng+1)]
        dage = [*one, *two] 
    else:
        dage = [{ "day": i, "val": None } for i in range(1,leng+1)]

    return {
        "month": dat.month,
        "num": leng,
        "days": dage,
        "offset": dat.weekday()
    }

def getMonthLength(num: int) -> int:
    names = [31,29,31,30,31,30,31,31,30,31,30,31]
    return names[num - 1]

def getNumDate(dat: str) -> list:
    day = int(dat[8:])
    month = int(dat[5:7])
    year = int(dat[0:4])
    return [year, month, day]

def getBinInfo(hab: BinHabit) -> dict:
    res = {}
    res["name"] = hab.name
    res["goal"] = hab.goal

    ents = BinEntry.objects.filter(habit=hab.id)
    res["num"] = len(ents)

    vals = [i.res for i in ents]
    res["vals"] = vals

    tot = 0
    for i in vals:
        tot += (1 if i else 0)
    res["curr"] = tot / len(ents)

    res["days"] = (hab.stop - hab.start).days
    res["left"] = res["days"] - res["num"]

    # needed
    # is_needed
    # left

    return res

def getNumInfo(hab: NumHabit) -> dict:
    res = {}
    res["name"] = hab.name
    res["goal"] = hab.goal

    ents = NumEntry.objects.filter(habit=hab.id)
    res["num"] = len(ents)

    vals = [i.res for i in ents]
    res["vals"] = vals

    tot = 0
    for i in vals:
        tot += (1 if i else 0)
    res["curr"] = tot / len(ents)

    res["days"] = (hab.stop - hab.start).days
    res["left"] = res["days"] - res["num"]
    
    return res