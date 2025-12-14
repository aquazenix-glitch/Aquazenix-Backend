from django.contrib import admin
from .models import Quote

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'service_type', 'created_at')
    search_fields = ('full_name', 'phone_number', 'description')
    list_filter = ('service_type', 'tank_size', 'created_at')
