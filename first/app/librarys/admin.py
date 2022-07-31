from django.contrib import admin
from .models import Librarys, LibrarysStorage, Librarian, LibrarysInLibrarian

'''list_display - какие атрибуты будут выводится на экран
list_display_links - какие атрибуты будут ссылками
search_fields - по каким полям будет происходить поиск
list_editable - какие поля можно изменить в таблице
list_filter - по каким полям будет происходить фильтр
fieldsets - настройки для страницы с изменениями'''


class LibrarysAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'librarys_name', 'librarys_address', 'description', 'id_librarys_storage', 'date_add', 'is_daleted'
    )
    list_display_links = ('id', 'librarys_name')
    search_fields = ('librarys_name', 'librarys_address')
    list_editable = ('is_daleted',)
    list_filter = ('librarys_name', 'is_daleted')
    fieldsets = (
        (None, {
            'fields': ('librarys_name', 'librarys_address', 'description', 'id_librarys_storage', 'library_img')
        }),
    )


class LibrarysStorageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'librarys_storage_address', 'date_creation', 'contact_phone',
        'email', 'website_linck', 'date_add', 'is_daleted'
    )
    list_display_links = ('id', 'librarys_storage_address',)
    search_fields = ('librarys_storage_address',)
    list_editable = ('is_daleted',)
    list_filter = ('date_add', 'is_daleted')
    fieldsets = (
        (
            (None, {
                'fields': ('librarys_storage_address',)
            }),

            ('Контакты', {
                'fields': ('date_creation', 'contact_phone', 'email', 'website_linck')
            })
        )
    )


class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'father_name', 'date_creation',
                    'birthday', 'home_address', 'contact_phone', 'email',
                    'date_add', 'is_daleted')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'last_name', 'father_name')
    list_editable = ('is_daleted',)
    list_filter = ('last_name', 'is_daleted')
    fieldsets = (
            (None, {
                'fields': ('first_name', 'last_name', 'father_name',
                           'date_creation', 'birthday', 'home_address', 'contact_phone', 'email',
                           'is_daleted')
            }),
    )

    inlines = [
        LibrarysInLibrarian,
    ]

admin.site.register(Librarys, LibrarysAdmin)
admin.site.register(LibrarysStorage, LibrarysStorageAdmin)
admin.site.register(Librarian, LibrarianAdmin)

