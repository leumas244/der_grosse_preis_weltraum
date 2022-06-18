from django import template

register = template.Library()


def switch_state(value):
    if value:
        value = False
    if not value:
        value = True
    return value


register.filter('switch_state', switch_state)
