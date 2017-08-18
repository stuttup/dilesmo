from django.contrib import admin

from .models import Queries
# Register your models here.

class QueriesAdmin(admin.ModelAdmin):
    fields = ['query']
    list_display = ('query',)

admin.site.register(Queries, QueriesAdmin)
