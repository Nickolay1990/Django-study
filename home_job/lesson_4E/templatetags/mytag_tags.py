from django import template
from lesson_4E.models import Games

register = template.Library()


@register.simple_tag(name='my_tag')
def total_games():
    queryset = Games.objects.all()
    even_list = []
    for i in queryset:
        if i.id % 2 == 0:
            even_list.append(i)
        if i.id % 10 == 0:
            i.color = True
    return even_list
