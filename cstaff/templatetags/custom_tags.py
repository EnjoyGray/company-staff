from django import template

register = template.Library()

@register.simple_tag
def toggle_ordering(current_ordering, field):
    if current_ordering == field:
        return f'-{field}'
    return field
