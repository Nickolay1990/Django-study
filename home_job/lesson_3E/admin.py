from django.contrib import admin
from .models import Games, Category, Sell


class GamesInstanceInline(admin.TabularInline):
    model = Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre')
    list_filter = ('name', )


@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'developer', 'platform')
    list_filter = ('platform',)
    inlines = [GamesInstanceInline]


@admin.register(Sell)
class SellAdmin(admin.ModelAdmin):
    list_display = ('sell', 'price', 'disc')
    list_filter = ('price', )
