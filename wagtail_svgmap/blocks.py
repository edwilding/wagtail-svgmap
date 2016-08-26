from __future__ import absolute_import, unicode_literals

from django.forms import Select
from django.utils.html import escape, mark_safe
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore import blocks
from wagtail_svgmap.models import ImageMap


class _ImageMapChoiceBlock(blocks.ChooserBlock):
    """
    Internal choice block; you shouldn't need to worry about this.
    """

    target_model = ImageMap
    widget = Select


class ImageMapBlock(blocks.StructBlock):
    """
    A StructBlock for StreamFields for choosing an ImageMap object and wrapping it in a CSS class.
    """

    map = _ImageMapChoiceBlock(required=True, label=_('Image map'))
    css_class = blocks.CharBlock(required=False, label=_('CSS class'))

    def render(self, value):
        if not value:  # pragma: no cover
            return ''

        image_map = value['map']
        if not image_map:  # pragma: no cover
            return ''
        assert isinstance(image_map, ImageMap)

        return mark_safe('<div class=\"image-map %(class)s\">%(svg)s</div>' % {
            'class': escape(value['css_class'] or ''),
            'svg': image_map.rendered_svg,
        })

    class Meta:
        icon = "image"
