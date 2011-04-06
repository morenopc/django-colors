from django.contrib import admin

from colors.models import Color, ColorGroup

class ColorAdmin(admin.ModelAdmin):
	"""
	A custom django admin interface for the color library
	"""
	pass

class ColorInline(admin.TabularInline):
	model = ColorGroup.colors.through


class ColorGroupAdmin(admin.ModelAdmin):
	"""
	A custom django admin interface for named color groups
	"""
	inlines=[ColorInline,]
	
admin.site.register(Color, ColorAdmin)
admin.site.register(ColorGroup, ColorGroupAdmin)