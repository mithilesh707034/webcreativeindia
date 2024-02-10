from django.contrib import admin
from .models import *
admin.site.register((Contact,Location,Service,Gallery,Blog,Ticket))

