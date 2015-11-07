from django.contrib import admin
from szobabeosztas.models import Camp, Room

class RoomInline(admin.StackedInline):
	model = Room
	extra = 1
	filter_horizontal = ('people',)

class CampAdmin(admin.ModelAdmin):
	inlines = [RoomInline]

admin.site.register(Camp, CampAdmin)

