from django.contrib import admin
from .models import *

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'time_created', 'time_updated')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'author')
admin.site.register(Recipe)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = 'name'
admin.site.register(Ingredient)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = 'name'
admin.site.register(Category)
