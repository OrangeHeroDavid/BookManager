from django import template

register = template.Library()


# from django.template import Library
# register = Library()

@register.inclusion_tag('pagenation.html')
def pagenation(num, current):
    return {"num": range(1, num + 1),
            "current": current}
