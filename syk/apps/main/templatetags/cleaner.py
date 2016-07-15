import bleach
from bs4 import BeautifulSoup
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def clearhtml(value):
    """
    :param value: html string
    :return: html with only whitelisted tags
    """
    whitelist_tags = ['a', 'i', 'b', 'u', 's', 'li', 'ul', 'ol', 'div', 'br']
    whitelist_attrs = {'a': ['href']}

    return bleach.clean(value, tags=whitelist_tags, attributes=whitelist_attrs)


@register.filter
@stringfilter
def disablelinks(value):
    soup = BeautifulSoup(value)
    for link in soup('a'):
        link.unwrap()
    return str(soup)
