from django.contrib import admin
from .models import *


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('content', 'title')


admin.site.register(Toping)
admin.site.register(Pizza, PizzaAdmin)
