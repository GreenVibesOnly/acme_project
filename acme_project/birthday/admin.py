from django.contrib import admin

from .models import Birthday, Tag


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (  # какие поля отображаются
        'first_name',
        'last_name',
        'author',
    )
    list_editable = (  # какие поля можно редактировать
        'author',
    )
    search_fields = ('first_name', 'last_name',)  # по каким полям можно искать запись
    list_filter = ('author',)  # по каким полям можно фильтровать записи
    list_display_links = ('first_name', 'last_name',)  # какие поля ведут на страницу с редакт записи


admin.site.register(Birthday, BirthdayAdmin)
admin.site.register(Tag)
