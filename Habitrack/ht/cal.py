from datetime import date

#* This is where we are going to define our months and days
#* which again brings up the question of how we're going to do this...
#* I think we first need a way to just populate the calendar for this year,
#* preferably in a semi dynamic way, just so that we don't have to hardcode 
#* everything from scratch (though that would be faster)

def getCal() -> dict:
    months = []

    for i in range(1,13):
        months[i] = makeCalItem(date(2024,i,1).weekday)
    
    return months

def makeCalItem(dat: date) -> dict:
    leng = getMonthLength(dat.month)
    dage = [{ "day": i, "val": None } for i in range(1,leng+1)]

    return {
        "Month": getMonthName(dat.month),
        "num": leng,
        "days": [],
        "offset": dat.weekday()
    }

def getMonthName(num: int) -> str:
    names = ["January", "Febraury", "March", "April", "May", "June", "July", 
             "August", "September", "October", "November", "December"]
    return names[num - 1]

def getMonthLength(num: int) -> int:
    names = [31,29,31,30,31,30,31,31,30,31,30,31]
    return names[num - 1]