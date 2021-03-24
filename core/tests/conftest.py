import pytest
from rest_framework.test import APIClient
from core.factories import PrivilegeFactory, RoleFactory, PersonFactory


@pytest.fixture
def privilege(db):
    return PrivilegeFactory()


@pytest.fixture
def role(db, privileges):
    return RoleFactory(privileges=privileges)


@pytest.fixture
def person(db, role):
    return PersonFactory(role=role)


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def privileges(db):
    return [PrivilegeFactory(), PrivilegeFactory(), PrivilegeFactory()]

