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

from django.test import TestCase
from mezzanine.pages.models import Page
from mezzanine.conf import settings as mez_settings
from django.conf import settings as django_settings
from django.template import Template, Context

from .models import DefaultImage, PageImage
from .templatetags.pageimage_tags import get_image_for_page


class TestGetImageForPage(TestCase):
    def setUp(self):
        self.p = Page(title='test')
        self.p.save()

    def setUpDefaultImage(self):
        di = DefaultImage(file='default.jpg', type='BACKGROUND')
        di.save()

    def setUpPageImage(self):
        pi = PageImage(page=self.p, type='BACKGROUND', file='test.jpg')
        pi.save()

    def test_get_empty(self):
        self.assertEqual(
            '',
            get_image_for_page(self.p, 'BACKGROUND')
        )

    def test_get_default_image(self):
        self.setUpDefaultImage()

        self.assertEqual(
            '/static/media/default.jpg',
            get_image_for_page(self.p, 'BACKGROUND')
        )

    def test_get_specific_image(self):
        self.setUpDefaultImage()
        self.setUpPageImage()

        self.assertEqual(
            '/static/media/test.jpg',
            get_image_for_page(self.p, 'BACKGROUND')
        )

    def test_get_child_images(self):
        self.setUpDefaultImage()
        self.setUpPageImage()

        p1 = Page.objects.create(title='child1', parent=self.p)
        p2 = Page.objects.create(title='child2', parent=self.p)

        PageImage.objects.create(page=p2, type='BACKGROUND', file='child2.jpg')

        self.assertEqual(
            '/static/media/test.jpg',
            get_image_for_page(p1, 'BACKGROUND')
        )
        self.assertEqual(
            '/static/media/child2.jpg',
            get_image_for_page(p2, 'BACKGROUND')
        )

    def test_get_banner_image(self):
        DefaultImage.objects.create(type='BANNER', file='defaultbanner.jpg')

        self.assertEqual(
            '/static/media/defaultbanner.jpg',
            get_image_for_page(self.p, 'BANNER')
        )


class TestPageImageTags(TestCase):
    def setUp(self):
        self.p = Page(title='test')
        self.p.save()

    def setUpTemplate(self):
        self.tmpl = Template(u'{% load pageimage_tags %}This will point to image \'{% pageimage \'BACKGROUND\' %}\'.')
        self.c = Context({'page': self.p})

    def test_simpletemplate_empty(self):
        self.setUpTemplate()
        tmplout = self.tmpl.render(self.c)
        self.assertTrue('\'\'' in tmplout)

    def test_simpletemplate_default(self):
        self.setUpTemplate()
        DefaultImage.objects.create(type='BACKGROUND', file='defaultback.jpg')
        self.assertTrue(
            '\'/static/media/defaultback.jpg\'' in self.tmpl.render(self.c)
        )

    def test_simpletemplate_specific(self):
        self.setUpTemplate()
        PageImage.objects.create(page=self.p, type='BACKGROUND', file='back.jpg')
        self.assertTrue(
            '\'/static/media/back.jpg\'' in self.tmpl.render(self.c)
        )


class TestSettings(TestCase):
    def test_mezannine_settings_exists(self):
        self.assertTrue(hasattr(mez_settings, 'PAGEIMAGE_TYPES'))
        #self.assertEqual(
            #mez_settings.PAGEIMAGE_TYPES[0][0],
            #'BACKGROUND'
        #)

    def test_django_settings_exists(self):
        self.assertTrue(hasattr(django_settings, 'PAGEIMAGE_TYPES'))
