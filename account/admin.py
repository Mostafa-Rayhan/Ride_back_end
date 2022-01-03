from django.contrib import admin
from .models import User
from .models import Review
from .models import Help
from .models import profileForm

# Register your models here.
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Help)
admin.site.register(profileForm)

# @admin.register(profileForm)
# class profileModelAdmin(admin.ModelAdmin):
#     list_display = ['firstName', 'lastName', 'email', 'phoneNumber', 'address', 'licence', 'nidNo', 'photo', 'gender']