mezzanine-pageimages
====================

Define (background-/banner-)images per page

# The Problem

At least our designer likes to create websites where pages can have individual
backgrounds. Or individual banners. So for example the index-page has a generic
background, while all pages under _Contact_ should have another background.

Mezzanine has this great feature that templates are searched by
`page-name.html`, `<content_type>.html` and then `page.html`. so one
would just create specific templates for the pages that get different
background. Its a nice solution that even works. But it has drawbacks:
 - To change the background, the designer has to ask the programmer because it
   can't be changed in the admin-backend.
 - When you have multiple child-pages which should all get the background of
   the parent-page, you end up with templates for each page.
 - When the designer or writer adds another page, the programmer has to add
   another template.

Mostly the problem is mixing content with design-code.

# The Solution

Here is how mezzanine-pageimages solves this:
 - In the admin-backend we just add a way to define images for certain roles
   and specific to certain pages. Plus a way to define default-images for the
   roles.
 - We define a template-tag `pageimage` that takes a role and the looks for
   the fitting image for the current page.
 - When there is no image for that role for the current page, it looks for an
   image on the parent page. It goes upwards until there is no parent or an
   image is found.
 - When there is still no image found, the default image for that role is
   returned, if there is one defined.

# Install

This package will be on pypi.python.org soon. Then its just a matter of `pip
install mezzanine-pageimage`.

Until then (and for development) either do a git-checkout and install via `pip
install -e`. Or you go by `pip install
git+https://github.com/bcs-de/mezzanine-pageimages.git#egg=mezzanine-pageimages`.

# Usage

Add the app to your `INSTALLED_APPS`. You can define your own image-roles in
the `SETTINGS` in settings.py:

```python
PAGEIMAGE_TYPES = (
    ('BACKGROUND', 'Description text'),
)
```

Then use it in your templates:

```
{% load pageimage_tages %}

Lets get the url for the background image: {% pageimage 'BACKGROUND' %}
```
