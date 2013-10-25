#
#   Copyright 2013 by Arnold Krille for bcs kommunikationsloesungen
#                     <a.krille@b-c-s.de>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from django import template
from ..models import DefaultImage

register = template.Library()

def get_default_image(type):
    defaultimgs = DefaultImage.objects.filter(type=type)
    if len(defaultimgs):
        return defaultimgs[0].file.url
    print "FALLBACK will return ''"
    return u''

def get_image_for_page(page, type):
    imgs = page.pageimage_set.filter(type=type)
    if len(imgs):
        return imgs[0].file.url
    if page.parent:
        return get_image_for_page(page.parent, type)
    return get_default_image(type)

@register.simple_tag(takes_context=True)
def pageimage(context, type):
    if 'page' in context:
        page = context['page']
        return get_image_for_page(page, type)
    return get_default_image(type)
