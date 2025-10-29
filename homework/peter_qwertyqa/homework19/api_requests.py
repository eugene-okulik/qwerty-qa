import requests


url = "http://objapi.course.qa-practice.com/object"


def get_object(id_obj):
    res = requests.get(url=f'{url}/{str(id_obj)}').json()
    return res


def post_new_object():
    headers = {'Content-Type': 'application/json'}
    data = {"name": "Test Object", "data": {"color": "black", "size": "big"}}
    res = requests.post(url=url, json=data, headers=headers).json()
    return res['id']


def delete_object(id_obj):
    res = requests.delete(url=f'{url}/{str(id_obj)}')
    print(res.text)


def post_object_test():
    headers = {'Content-Type': 'application/json'}
    data = {"name": "Test Object", "data": {"color": "black", "size": "big"}}
    res = requests.post(url=url, json=data, headers=headers)
    print(res.json())
    assert res.status_code == 200, 'Status code is incorrect'
    assert res.json()['name'] == data["name"]
    delete_object(res.json()["id"])


def put_object_test():
    id_obj = post_new_object()
    data = {"name": "Test Object 2",
            "data": {"color": "greeeeeey", "size": "small"}}
    res = requests.put(url=f'{url}/{str(id_obj)}', json=data)
    print(res.json())
    assert res.status_code == 200, 'Status code is incorrect'
    assert res.json()["name"] == data["name"]
    delete_object(res.json()["id"])


def patch_object_test():
    id_obj = post_new_object()
    data = {"name": "Test Object 335"}
    res = requests.patch(url=f'{url}/{str(id_obj)}', json=data)
    print(res.json())
    assert res.status_code == 200, 'Status code is incorrect'
    assert res.json()["name"] == data["name"]
    delete_object(res.json()["id"])


def delete_object_test():
    id_obj = post_new_object()
    res = requests.delete(url=f'{url}/{str(id_obj)}')
    print(res.text)
    assert res.status_code == 200, 'Status code is incorrect'


post_object_test()
put_object_test()
patch_object_test()
delete_object_test()
