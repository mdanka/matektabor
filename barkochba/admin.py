from django.contrib import admin
from barkochba.models import Person, Story

class StoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'order_number')

admin.site.register(Story, StoryAdmin)
admin.site.register(Person)
