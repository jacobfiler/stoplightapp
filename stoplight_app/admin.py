from django.contrib import admin
from .models import ReformArea, Reform, State, SourceType, Source, ReformStatus

class SourceInline(admin.TabularInline):
    model = Source
    extra = 1

@admin.register(ReformStatus)
class ReformStatusAdmin(admin.ModelAdmin):
    search_fields = ['reform__name', 'state__name']
    list_filter = ['status', 'state']
    list_display = ['reform', 'state', 'status', 'last_updated']
    list_select_related = ['reform', 'state']
    autocomplete_fields = ['reform', 'state']
    inlines = [SourceInline]

@admin.register(Reform)
class ReformAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'slcid', 'reform_area', 'last_updated']
    list_filter = ['reform_area']
    autocomplete_fields = ['reform_area']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    search_fields = ['name']
    autocomplete_fields = []

@admin.register(SourceType)
class SourceTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    autocomplete_fields = []

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    search_fields = ['reform_status__reform__name', 'source_type__name']
    list_display = ['reform_status', 'source_type', 'url']
    list_select_related = ['reform_status', 'source_type']
    autocomplete_fields = ['reform_status', 'source_type']

@admin.register(ReformArea)
class ReformAreaAdmin(admin.ModelAdmin):
    search_fields = ['name']
    autocomplete_fields = []

