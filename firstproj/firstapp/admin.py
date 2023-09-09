from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MenuCategory)
admin.site.register(Menu)

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User 

admin.register(User)
class NewAdmin(UserAdmin): 
    readonly_fields = [ 
        'date_joined', 
    ]
    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs) 
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True 

        return form
    
@admin.register(Person) 
class PersonAdmin(admin.ModelAdmin): 
    list_display = ("first_name", "last_name")
    search_fields = ("first_name__startswith", )