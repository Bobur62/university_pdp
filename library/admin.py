from django.contrib import admin
from .models import Book, User, BookRecord


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'colored_name')


# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    # fields = ('title', 'author', 'count')
    fields = (('title', 'author'), 'count')
    # exclude = ('author',) #admindan paneldan modelfieldni olib tashlaydi
    list_display = ('title', 'author', 'count')
    # list_display_links = ('title', 'author', 'count')
    # list_display_links = None
    list_filter = ('author',)
    # list_select_related = ('title', 'author') list_max_show_all = () ordering = ['date_created']
    # autocomplete_fields = ['title'] #ForeignKey da ishlatamiz search qo'shib beradi raw_id_fields = ("title",
    # ) #text fieldlarda ishlatamiz search qilishni qo'shadi --> ForeignKey & ManyToManyField da ishlatamiz save_as =
    # False #bu orqali fialed obectlarni bir pageni o'zida qayta qayta save yangilarini save qilishga yordam beradi
    # save_on_top = False view_on_site = False
    search_fields = ['title__icontains', 'count']

    # class Media:
    #     css = {
    #         "all": ("my_styles.css",)
    #     }
    #     js = ("my_code.js",)

    # InlineModelAdmin options¶******************


# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role')
    list_filter = ('role',)
    fields = ('role', ('first_name', 'last_name'))
    search_fields = ('first_name',)


def mark_book_as_returned(modeladmin, request, queryset):
    for book_record in queryset:
        print(book_record.book, book_record.user)


# admin.site.register(BookRecord)
@admin.register(BookRecord)
class BookRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'took_on', 'is_returned')
    list_filter = ('user',)
    # search_fields = ("user",)
    fields = ('user', 'book', ('took_on', 'returned_on'))
    #     search_fields = ('first_name',)
    autocomplete_fields = ("book", "user")
    list_select_related = ("book",
                           "user",)  # ForenKay da ishlatsak adminga databasedan malumotlarni wrap qilib olinadi
    # barchasi yani har biri uchun queary jo'natishni oldini oladi
    actions = (mark_book_as_returned,)

# @admin.display(description='Name')
# def upper_case_name(obj):
#     return ("%s %s" % (obj.first_name, obj.last_name)).upper()
#
# class PersonAdmin(admin.ModelAdmin):
#     list_display = (upper_case_name,)
