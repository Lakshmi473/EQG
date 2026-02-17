from django.contrib import admin

# Register your models here.

from .models import Category, Company, Item

admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Item)