from datetime import date


# /////////////////////////////////////////////////////////
# POST
# /////////////////////////////////////////////////////////
def test_create_person_success(client, db, role):
    data = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'firstname@lastname.com',
        'birth_date': date.today(),
        'role': 1
    }

    request = client.post('/person/new/', data)

    assert request.status_code == 201
    assert request.json()['first_name'] == 'first_name'
    assert request.json()['email'] == 'firstname@lastname.com'
    assert request.json()['birth_date'] == '2021-03-24'


def test_create_person_error_no_data_provided(client, db):
    data = {
    }

    request = client.post('/person/new/', data)
    assert request.status_code == 400
    assert request.json() == {
        'birth_date': ['This field is required.'],
        'email': ['This field is required.'],
        'first_name': ['This field is required.'],
        'last_name': ['This field is required.'],
        'role': ['This field is required.']
    }


def test_create_person_error_not_valid_role(client, db):
    data = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'firstname@lastname.com',
        'birth_date': date.today(),
        'role': 'role'
    }

    request = client.post('/person/new/', data)
    assert request.status_code == 400
    assert request.json() == {'role': ['Incorrect type. Expected pk value, received str.']}


def test_create_person_error_role_does_not_exist(client, db):
    data = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'firstname@lastname.com',
        'birth_date': date.today(),
        'role': 1
    }

    request = client.post('/person/new/', data)
    assert request.status_code == 400
    assert request.json() == {'role': ['Invalid pk "1" - object does not exist.']}


def test_create_person_error_empty_strings_provided(client, db, role):
    data = {
        'first_name': '',
        'last_name': '',
        'email': 'firstname@lastname.com',
        'birth_date': date.today(),
        'role': 1
    }

    request = client.post('/person/new/', data)

    assert request.status_code == 400
    assert request.json() == {'first_name': ['This field may not be blank.'],
                              'last_name': ['This field may not be blank.']
                              }


# /////////////////////////////////////////////////////////
# GET
# /////////////////////////////////////////////////////////
def test_get_one_person_success(client,  person):
    request = client.get('/person/1/')

    assert request.status_code == 200
    assert request.json()['id'] == 1


def test_incorrect_url(client):
    request = client.get('/people/')
    assert request.status_code == 404


def test_person_detail_success(client, person):
    request = client.get('/person/1/')
    assert request.status_code == 200
    assert request.json()['id'] == 1


def test_person_fail_does_not_exist(client, db):
    request = client.get(f'/person/11/')
    assert request.status_code == 404
    assert {'detail': 'Not found.'}


def test_person_roles_and_privileges(person):
    assert person.role.privileges.first().id == 1
    assert person.role.privileges.get(id=2).id == 2
    assert person.role.privileges.last().id == 3
    assert person.role.id == 1


# /////////////////////////////////////////////////////////
# DELETE
# /////////////////////////////////////////////////////////
def test_delete_success(client, db, person):
    request = client.delete('/person/1/')
    assert request.status_code == 204


def test_delete_fail_does_not_exist(client, db):
    request = client.delete('/person/1000000/')
    assert request.status_code == 404


# /////////////////////////////////////////////////////////
# PATCH
# /////////////////////////////////////////////////////////
def test_patch_name_success(client, db, person):
    data = {
        'first_name': 'AlekefromKz'
    }
    request = client.patch('/person/1/', data)
    assert request.status_code == 200
    assert request.json()['first_name'] == 'AlekefromKz'


# why the same role is provided?
def test_patch_level_role(client, db, person, role):
    print(person.role.__dict__)
    print(role.__dict__)
    data = {
        'role': role.id
    }
    request = client.patch('/person/1/', data)
    assert request.status_code == 200


def test_patch_id_success_does_not_change(client, db, person):
    data = {
        'id': 10
    }
    request = client.patch('/person/1/', data)
    assert request.status_code == 200
    assert request.json()['id'] == 1


def test_patch_field_success_field_does_not_exist(client, db, person):
    data = {
        'ssd': 'absent'
    }
    request = client.patch('/person/1/', data)
    assert request.status_code == 200


def test_patch_field_fail_bad_request(client, db, person):
    data = {
        'last_name': 'Salem'
    }
    request = client.patch('/person/10000/', data)
    assert request.status_code == 404


# /////////////////////////////////////////////////////////
# PUT
# /////////////////////////////////////////////////////////
def test_put_success(client, db, person):
    data = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'firstname@lastname.com',
        'birth_date': date.today(),
        'role': 1
    }
    request = client.put('/person/1/', data)
    assert request.status_code == 200
    assert request.json()['id'] == 1
    assert request.json()['first_name'] == 'first_name'
    assert request.json()['role'] == 1


def test_put_success_not_needed_argument_provided(client, db, person):
    data = {
        'ssd': 512,
        'os': 'ubuntu',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'firstname@lastname.com',
        'birth_date': date.today(),
        'role': 1
    }
    request = client.put('/person/1/', data)
    assert request.status_code == 200
    assert request.json()['id'] == 1
    assert request.json()['first_name'] == 'first_name'
    assert request.json()['role'] == 1


def test_put_name_fail_not_all_arguments_provided(client, db, person):
    data = {
        'id': 1
    }
    request = client.put('/person/1/', data)
    assert request.status_code == 400


def test_put_name_fail_bad_request(client, db):
    data = {
        'name': 'name'
    }
    request = client.put('/persons/1/', data)
    assert request.status_code == 404


def test_put_name_fail_bad_request_again(client, db):
    data = {
        'name': 'AlekefromKz'
    }
    request = client.put('/person/111/', data)
    assert request.status_code == 404
