from django import template

register = template.Library()

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