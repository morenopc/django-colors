from django.db import models
from django.utils.translation import ugettext as _

from colors.fields import ColorField

class Color(models.Model):
	"""
	A unique color in the color library
	"""
	color = ColorField(_(u"color code"), unique=True)
	
	def __unicode__(self):
		return self.color


class ColorGroup(models.Model):
	"""
	A named group of colors, e.g. 'Black & White' which contains
	the FFF and 000 hex colors
	"""
	name = models.CharField(max_length=25)
	colors = models.ManyToManyField("Color", related_name="color_groups")

	def __unicode__(self):
		return self.name