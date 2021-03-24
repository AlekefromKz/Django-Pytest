from django.contrib import admin
from .models import Privilege, Role, Person

admin.site.register(Privilege)
admin.site.register(Role)
admin.site.register(Person)
