import requests
import pytest
import allure


url = "http://objapi.course.qa-practice.com/object"


def get_object(id_obj):
    res = requests.get(url=f'{url}/{str(id_obj)}').json()
    return res


@pytest.fixture(scope='session')
def start_end():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture()
def new_post_object():
    print("\nbefore test")
    headers = {'Content-Type': 'application/json'}
    data = {"name": "Test Object", "data": {"color": "black", "size": "big"}}
    res = requests.post(url=url, json=data, headers=headers).json()
    yield res
    requests.delete(url=f"{url}/{str(res['id'])}")
    print("\nafter test")


@allure.feature('Posts feature')
@allure.story('Create posts story')
@pytest.mark.critical
@pytest.mark.parametrize('data', [{"name": "Test Object 1",
                                   "data": {"color": "black",
                                            "size": "big"}},
                                  {"name": "Test Object 2",
                                   "data": {"color": "black",
                                            "size": "big"}},
                                  {"name": "Test Object 3",
                                   "data": {"color": "black",
                                            "size": "big"}}])
def test_post_object(data, start_end, new_post_object):
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url=url, json=data, headers=headers)
    assert res.status_code == 200, 'Status code is incorrect'
    assert res.json()['name'] == data["name"]
    requests.delete(url=f"{url}/{str(res.json()['id'])}")


@allure.feature('Posts feature')
@allure.story('Change posts story')
@allure.title('Put new data into object')
@pytest.mark.medium
def test_put_object(new_post_object):
    with allure.step('Prepare data'):
        data = {"name": "Test Object 2",
                "data": {"color": "greeeeeey", "size": "small"}}
    with allure.step('Send PUT request'):
        res = requests.put(url=f"{url}/{str(new_post_object['id'])}",
                           json=data)
    with allure.step('Check if the status code is 200'):
        assert res.status_code == 200, 'Status code is incorrect'
    with allure.step('Check if name in response is equal to the name from requestsq'):
        assert res.json()["name"] == data["name"]


@allure.feature('Posts feature')
@allure.story('Change posts story')
def test_patch_object(new_post_object):
    data = {"name": "Test Object 335"}
    res = requests.patch(url=f"{url}/{str(new_post_object['id'])}",
                         json=data)
    assert res.status_code == 200, 'Status code is incorrect'
    assert res.json()["name"] == data["name"]


@allure.feature('Delete feature')
def test_delete_object(new_post_object):
    res = requests.delete(url=f"{url}/{str(new_post_object['id'])}")
    assert res.status_code == 200, 'Status code is incorrect'
