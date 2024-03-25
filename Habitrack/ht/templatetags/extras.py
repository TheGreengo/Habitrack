from django import template

register = template.Library()

@register.filter(name="diff")
def doub(thing):
    value = abs(thing["curr"] - thing["goal"])
    return f"{value:.2f}"

@register.filter(name="doub")
def doub(value):
    return f"{value:.2f}"

@register.filter(name="range")
def cut(value):
    return range(value)

@register.filter(name="colors")
def cut(value):
    if (value <= 0.34):
        return 0
    if (value <= 0.67):
        return 1
    return 2

@register.filter(name="bins")
def cut(value):
    if value != "success":
        return 0
    return 2

@register.filter(name="dates")
def cut(month, day):
    return (month*100)+day

@register.filter(name="months")
def cut(ind):
    names = ["January", "February", "March", "April", "May", "June", "July", 
        "August", "September", "October", "November", "December"]
    return names[ind - 1]
    
# ! I don't think we're going to end up using this for now
@register.filter(name="nums")
def cut(goal, value, kind):
    if (kind == "less" and value > goal) or \
    (kind == "more" and value < goal):
        return 0
    return 2