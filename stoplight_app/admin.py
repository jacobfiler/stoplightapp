from django.contrib import admin
from .models import ReformArea, Reform, State, ReformStatus, SourceType, Source

class SourceInline(admin.TabularInline):
    model = Source
    extra = 1

class ReformStatusAdmin(admin.ModelAdmin):
    list_display = ('reform', 'state', 'status', 'additional_notes', 'last_updated')  # Include last_updated as well
    inlines = [SourceInline]

admin.site.register(ReformArea)
admin.site.register(Reform)
admin.site.register(State)
admin.site.register(ReformStatus, ReformStatusAdmin)
admin.site.register(SourceType)
admin.site.register(Source)
