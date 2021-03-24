# POST
def test_create_privilege_success(client, db):
    data = {
        'level': 10,
        'name': 'privilege'
    }

    request = client.post('/privilege/new/', data)
    assert request.status_code == 201
    assert request.json()['id'] == 1
    assert request.json()['name'] == 'privilege'
    assert 1 <= request.json()['level'] <= 10


def test_create_privilege_success_level_name_is_int(client, db):
    data = {
        'name': 123,
        'level': 123
    }

    request = client.post('/privilege/new/', data)
    assert request.status_code == 201


def test_create_privilege_error_no_level(client, db):
    data = {
        'name': 'privilege'
    }

    request = client.post('/privilege/new/', data)
    assert request.status_code == 400
    assert request.json() == {'level': ['This field is required.']}


def test_create_privilege_error_no_name(client, db):
    data = {
        'level': 1
    }

    request = client.post('/privilege/new/', data)
    assert request.status_code == 400
    assert request.json() == {'name': ['This field is required.']}


def test_create_privilege_error_level_is_int(client, db):
    data = {
        'name': 'role',
        'level': 'string'
    }

    request = client.post('/privilege/new/', data)
    assert request.status_code == 400
    assert request.json() == {'level': ['A valid integer is required.']}


def test_create_privilege_error_empty_strings_provided(client, db):
    data = {
        'name': '',
        'level': ''
    }

    request = client.post('/privilege/new/', data)

    assert request.status_code == 400
    assert request.json() == {'level': ['A valid integer is required.'], 'name': ['This field may not be blank.']}


# GET
def test_get_one_privilege_success(privilege, client,  db):
    request = client.get('/privilege/1/')
    assert request.status_code == 200
    assert request.json()['id'] == 1


def test_incorrect_url(client):
    request = client.get('/privileges/')
    assert request.status_code == 404


def test_privilege_detail_success(client, privilege):
    request = client.get(f'/privilege/{privilege.id}/')
    assert request.status_code == 200


def test_privilege_fail_does_not_exist(client, db):
    request = client.get(f'/privilege/{100000000}/')
    assert request.status_code == 404
    assert {'detail': 'Not found.'}


def test_level_range(privilege):
    assert 1 <= privilege.level <= 10


def test_name_is_string(privilege):
    assert isinstance(privilege.name, str)


# DELETE
def test_delete_success(client, db, privilege):
    request = client.delete('/privilege/1/')
    assert request.status_code == 204


def test_delete_fail_does_not_exist(client, db):
    request = client.delete('/privilege/10000000000/')
    assert request.status_code == 404


# PATCH
def test_patch_name_success(client, db, privilege):
    data = {
        'name': 'AlekefromKz'
    }
    request = client.patch('/privilege/1/', data)
    assert request.status_code == 200
    assert request.json()['name'] == 'AlekefromKz'


def test_patch_level_success(client, db, privilege):
    data = {
        'level': 9
    }
    request = client.patch('/privilege/1/', data)
    assert request.status_code == 200
    assert request.json()['level'] == 9


def test_patch_id_success_does_not_change(client, db, privilege):
    data = {
        'id': 10
    }
    request = client.patch('/privilege/1/', data)
    assert request.status_code == 200
    assert request.json()['id'] == 1


def test_patch_field_success_field_does_not_exist(client, db, privilege):
    data = {
        'last_name': 'Salem'
    }
    request = client.patch('/privilege/1/', data)
    assert request.status_code == 200


def test_patch_field_fail_bad_request(client, db, privilege):
    data = {
        'last_name': 'Salem'
    }
    request = client.patch('/privilege/10000/', data)
    assert request.status_code == 404


# PUT
def test_put_success(client, db, privilege):
    data = {
        'id': 1000,
        'level': 7,
        'name': 'AlekefromKz'
    }
    request = client.put('/privilege/1/', data)
    assert request.status_code == 200
    assert request.json()['id'] == 1
    assert request.json()['level'] == 7
    assert request.json()['name'] == 'AlekefromKz'


def test_put_success_not_needed_argument_provided(client, db, privilege):
    data = {
        'ssd': 512,
        'os': 'ubuntu',
        'id': 1000,
        'level': 7,
        'name': 'AlekefromKz'
    }
    request = client.put('/privilege/1/', data)
    assert request.status_code == 200
    assert request.json()['id'] == 1
    assert request.json()['level'] == 7
    assert request.json()['name'] == 'AlekefromKz'


def test_put_name_fail_not_all_arguments_provided(client, db, privilege):
    data = {
        'name': 'AlekefromKz'
    }
    request = client.put('/privilege/1/', data)
    assert request.status_code == 400


def test_put_name_fail_bad_request(client, db, privilege):
    data = {
        'name': 'AlekefromKz'
    }
    request = client.put('/privileges/1/', data)
    assert request.status_code == 404


def test_put_name_fail_bad_request_again(client, db, privilege):
    data = {
        'name': 'AlekefromKz'
    }
    request = client.put('/privilege/111/', data)
    assert request.status_code == 404
