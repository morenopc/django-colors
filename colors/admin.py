from django.contrib import admin

from colors.models import Color, ColorGroup

class ColorAdmin(admin.ModelAdmin):
	"""
	A custom django admin interface for the color library
	"""
	pass


class ColorGroupAdmin(admin.ModelAdmin):
	"""
	A custom django admin interface for named color groups
	"""
	pass
	
admin.site.register(Color, ColorAdmin)
admin.site.register(ColorGroup, ColorGroupAdmin)