from django.urls import path
from . import views


privilege_patterns = [
    path('', views.PrivilegeView.as_view()),
    path('new/', views.PrivilegeCreate.as_view()),
    path('<int:pk>/', views.PrivilegeRetrieveUpdateDestroyPK.as_view()),
    path('<str:name>/', views.PrivilegeRetrieveUpdateDestroyName.as_view()),
]


role_patterns = [
    path('', views.RoleView.as_view()),
    path('new/', views.RoleCreate.as_view()),
    path('<int:pk>/', views.RoleRetrieveUpdateDestroyPK.as_view()),
]


person_patterns = [
    path('', views.PersonView.as_view()),
    path('new/', views.PersonCreate.as_view()),
    path('<int:pk>/', views.PersonRetrieveUpdateDestroyPK.as_view()),
]
