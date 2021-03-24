from django.contrib import admin
from django.urls import path, include
from core.urls import privilege_patterns, role_patterns, person_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('privilege/', include(privilege_patterns)),
    path('role/', include(role_patterns)),
    path('person/', include(person_patterns)),
]
