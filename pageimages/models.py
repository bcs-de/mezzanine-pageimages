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

from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page
from mezzanine.core.fields import FileField
from mezzanine.utils.models import upload_to
from mezzanine.conf import settings

# Create your models here.

class PageImage(models.Model):
    page = models.ForeignKey(Page)
    file = FileField(_("File"), max_length=200, format="Image",
        upload_to=upload_to("galleries.GalleryImage.file", ""))
    type = models.CharField(max_length=32, choices=settings.PAGEIMAGE_TYPES)

    class Meta:
        verbose_name = _('Page-Image')
        verbose_name_plural = _('Pages Images')

class DefaultImage(models.Model):
    file = FileField(_("File"), max_length=200, format="Image",
        upload_to=upload_to("galleries.GalleryImage.file", ""))
    type = models.CharField(max_length=32, choices=settings.PAGEIMAGE_TYPES)
