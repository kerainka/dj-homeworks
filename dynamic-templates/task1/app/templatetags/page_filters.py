from django import template


register = template.Library()


@register.filter
def color(value):
    if value is None:
        return 'white'
    elif value < 0:
        return 'green'
    elif value < 1:
        return 'white'
    elif value < 2:
        return '#fca8ad'
    elif value < 5:
        return '#fb747b'
    return '#f70d1a'
