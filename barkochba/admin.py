from django.contrib import admin
from barkochba.models import Story

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'order_number')
    exclude = ('people',)

admin.site.register(Story, StoryAdmin)

