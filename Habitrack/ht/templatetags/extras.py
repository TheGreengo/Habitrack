from django import template

register = template.Library()

@register.filter(name="range")
def cut(value):
    return range(value)

@register.filter(name="colors")
def cut(value):
    if (value <= 0.25):
        return 0
    if (value <= 0.50):
        return 1
    if (value <= 0.75):
        return 2
    return 3