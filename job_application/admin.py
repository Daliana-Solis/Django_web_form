from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email") #show on admin homepage
    search_fields = ("first_name", "last_name", "email") #search bar can search for those fields
    list_filter = ("date", "occupation") #filter by date or occupation
    ordering = ("first_name", ) #order by ...
    readonly_fields = ("occupation", ) #read only, cannot change that field admin view


admin.site.register(Form, FormAdmin)