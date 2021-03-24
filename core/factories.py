from random import randint
import factory
from .models import Privilege, Role, Person


class PrivilegeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Privilege

    level = factory.LazyFunction(lambda: randint(1, 10))
    name = factory.Faker('word')


class RoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Role
        
    name = factory.Faker('word')

    @factory.post_generation
    def privileges(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for privilege in extracted:
                self.privileges.add(privilege)


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    birth_date = factory.Faker('date_object')
    # role = factory.SubFactory(RoleFactory)
    # decided to provide a role as an argument in configure test
