from django.contrib import admin
from .models import Shoe, Worn, Shoelace
# Register your models here.
admin.site.register(Shoe)
admin.site.register(Worn)
admin.site.register(Shoelace)