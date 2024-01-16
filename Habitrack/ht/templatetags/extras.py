from django import template

register = template.Library()

@register.filter(name="range")
def cut(value):
    return range(value)