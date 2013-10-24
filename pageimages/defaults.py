
from mezzanine.conf import register_setting

register_setting(
    name="PAGEIMAGE_TYPES",
    description="The list of image types defined by pageimages and used in the templates.",
    editable=False,
    default=(
        ('BACKGROUND', 'Background image for the page'),
    ),
)
