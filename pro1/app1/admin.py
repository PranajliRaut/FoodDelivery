from django.contrib import admin

from .models import Contact, Category, Team, Dish, Profile,Order
# Register your models here.


admin.site.site_header = "FoodZone | Admin"
admin.site.site_title = "FoodZone Admin Portal"
admin.site.index_title = "Welcome to FoodZone Administration"


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','added_on','is_approved']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']

class DishAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','added_on','updated_on']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Team, TeamAdmin )
admin.site.register(Dish, DishAdmin )
admin.site.register(Profile)
admin.site.register(Order)
