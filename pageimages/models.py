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
