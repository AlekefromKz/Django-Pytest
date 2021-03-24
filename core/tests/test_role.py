# /////////////////////////////////////////////////////////
# POST
# /////////////////////////////////////////////////////////
def test_create_role_success(client, db, privileges):
    data = {
        'name': 'role',
        'privileges': [1, 2, 3]
    }

    request = client.post('/role/new/', data)
    assert request.status_code == 201
    assert request.json() == {
        'id': 1,
        'name': 'role',
        'privileges': [1, 2, 3]
    }


def test_create_role_error_no_level(client, db):
    data = {
        'name': 'role'
    }

    request = client.post('/role/new/', data)
    assert request.status_code == 400
    assert request.json() == {'privileges': ['This list may not be empty.']}


def test_create_role_error_not_valid_privileges(client, db):
    data = {
        'name': 'role',
        'privileges': ['aleke', 'bake', 'make']
    }

    request = client.post('/role/new/', data)
    assert request.status_code == 400
    assert request.json() == {'privileges': ['Incorrect type. Expected pk value, received str.']}


def test_create_role_error_privileges_do_not_exist(client, db):
    data = {
        'name': 'role',
        'privileges': [1, 2, 3]
    }

    request = client.post('/role/new/', data)
    assert request.status_code == 400
    assert request.json() == {'privileges': ['Invalid pk "1" - object does not exist.']}


def test_create_role_error_empty_strings_provided(client, db):
    data = {
        'name': '',
        'level': ''
    }

    request = client.post('/role/new/', data)

    assert request.status_code == 400
    assert request.json() == {'name': ['This field may not be blank.'], 'privileges': ['This list may not be empty.']}


# /////////////////////////////////////////////////////////
# GET
# /////////////////////////////////////////////////////////
def test_get_one_role_success(role, client,  db):
    request = client.get('/role/1/')

    assert request.status_code == 200
    assert request.json()['id'] == 1


def test_incorrect_url(client):
    request = client.get('/roles/')
    assert request.status_code == 404


def test_role_detail_success(client, role):
    request = client.get(f'/role/{role.id}/')
    assert request.status_code == 200
    assert request.json()['id'] == 1


def test_role_fail_does_not_exist(client, db):
    request = client.get(f'/role/100000000/')
    assert request.status_code == 404
    assert {'detail': 'Not found.'}


def test_privileges_1_2_3(client, db, role):
    assert role.privileges.first().id == 1
    assert role.privileges.get(id=2).id == 2
    assert role.privileges.last().id == 3


# /////////////////////////////////////////////////////////
# DELETE
# /////////////////////////////////////////////////////////
def test_delete_success(client, db, role):
    request = client.delete('/role/1/')
    assert request.status_code == 204


def test_delete_fail_does_not_exist(client, db):
    request = client.delete('/role/10000000000/')
    assert request.status_code == 404


# /////////////////////////////////////////////////////////
# PATCH
# /////////////////////////////////////////////////////////
def test_patch_name_success(client, db, role):
    data = {
        'name': 'AlekefromKz'
    }
    request = client.patch('/role/1/', data)
    assert request.status_code == 200
    assert request.json()['name'] == 'AlekefromKz'


def test_patch_level_success(client, db, role):
    data = {
        'privileges': [1, 2]
    }
    request = client.patch('/role/1/', data)
    assert request.status_code == 200


def test_patch_id_success_does_not_change(client, db, role):
    data = {
        'id': 10
    }
    request = client.patch('/role/1/', data)
    assert request.status_code == 200
    assert request.json()['id'] == 1


def test_patch_field_success_field_does_not_exist(client, db, role):
    data = {
        'last_name': 'Salem'
    }
    request = client.patch('/role/1/', data)
    assert request.status_code == 200


def test_patch_field_fail_bad_request(client, db, role):
    data = {
        'last_name': 'Salem'
    }
    request = client.patch('/role/10000/', data)
    assert request.status_code == 404


# /////////////////////////////////////////////////////////
# PUT
# /////////////////////////////////////////////////////////
def test_put_success(client, db, role):
    data = {
        'id': 1000,
        'name': 'AlekefromKz',
        'privileges': [3]
    }
    request = client.put('/role/1/', data)
    assert request.status_code == 200
    assert request.json()['id'] == 1
    assert request.json()['name'] == 'AlekefromKz'
    assert request.json()['privileges'] == [3]


def test_put_success_not_needed_argument_provided(client, db, role):
    data = {
        'ssd': 512,
        'os': 'ubuntu',
        'id': 1000,
        'level': 7,
        'name': 'AlekefromKz',
        'privileges': [1, 3]
    }
    request = client.put('/role/1/', data)
    assert request.status_code == 200
    assert request.json()['id'] == 1
    assert request.json()['name'] == 'AlekefromKz'
    assert request.json()['privileges'] == [1, 3]


def test_put_name_fail_not_all_arguments_provided(client, db, role):
    data = {
        'name': 'AlekefromKz'
    }
    request = client.put('/role/1/', data)
    assert request.status_code == 400


def test_put_name_fail_bad_request(client, db):
    data = {
        'name': 'AlekefromKz'
    }
    request = client.put('/roles/1/', data)
    assert request.status_code == 404


def test_put_name_fail_bad_request_again(client, db, role):
    data = {
        'name': 'AlekefromKz'
    }
    request = client.put('/role/111/', data)
    assert request.status_code == 404
