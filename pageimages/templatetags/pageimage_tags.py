
from django import template
from ..models import DefaultImage

register = template.Library()

def get_image_for_page(page, type):
    imgs = page.pageimage_set.filter(type=type)
    if len(imgs):
        return imgs[0].file.url
    if page.parent:
        return get_image_for_page(page.parent, type)
    defaultimgs = DefaultImage.objects.filter(type=type)
    if len(defaultimgs):
        return defaultimgs[0].file.url
    print "FALLBACK will return ''"
    return u''

@register.simple_tag(takes_context=True)
def pageimage(context, type):
    print u"Should return an image-url for type '{}' on context '{}'".format(type, context['page'])
    page = context['page']
    return get_image_for_page(page, type)
