from django import template

register = template.Library()


@register.filter
def media(image):
    if image:
        return f'/media/{image}'

    return '#'