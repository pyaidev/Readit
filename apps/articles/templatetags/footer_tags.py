from django import template

from ..models import Article

register = template.Library()

@register.simple_tag()
def footer_tags():
    last_2_article = Article.objects.all().order_by('-id')[:2]
    return last_2_article
