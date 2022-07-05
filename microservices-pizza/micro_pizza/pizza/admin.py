from django.contrib import admin
from .models import *
# Register your models here.

class PizzeriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner','address','phone')

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','description', 'thumbnail_url','approved','creator')

class LikesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','pizza')

admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Pizzeria, PizzeriaAdmin)
admin.site.register(Likes, LikesAdmin)