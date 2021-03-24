from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import PrivilegeSerializer, RoleSerializer, PersonSerializer
from .models import Privilege, Role, Person


# //////////////////
# LIST VIEWS
# //////////////////
class PrivilegeView(ListAPIView):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer


class RoleView(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class PersonView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


# //////////////////
# RETRIEVE | UPDATE | DESTROY VIEWS
# //////////////////

# LEARN TO FILTER BY TWO FIELDS IN ONE CLASS
class PrivilegeRetrieveUpdateDestroyPK(RetrieveUpdateDestroyAPIView):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer
    lookup_field = 'pk'


# LEARN TO FILTER BY TWO FIELDS IN ONE CLASS
class PrivilegeRetrieveUpdateDestroyName(RetrieveUpdateDestroyAPIView):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer
    lookup_field = 'name'


class RoleRetrieveUpdateDestroyPK(RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    lookup_field = 'pk'


class PersonRetrieveUpdateDestroyPK(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'pk'


# //////////////////
# CREATE VIEWS
# //////////////////
class PrivilegeCreate(CreateAPIView):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer


class RoleCreate(CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class PersonCreate(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
