from django import template

register = template.Library()


# truncate a word by the length l
@register.filter(name='shortify')
def shortify(word, l=2):
    return word[:2].upper()
