from django.contrib import admin

from .models import Bb, Rubric
# Register your models here.


class BbAdmin(admin.ModelAdmin):
    list_display = ('title',  'price', 'rubric', 'published')
    list_display_links = ('title', 'rubric')
    search_fields = ('title', 'content')


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
