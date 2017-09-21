from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(IdentificationType)
admin.site.register(GenderType)
admin.site.register(Cities)
admin.site.register(AuthDiscountRouster)