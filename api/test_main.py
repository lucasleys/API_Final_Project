import requests
import json

headers = {
"accept": "application/json",
"Content-Type": "application/json"
}

tokenrequest = requests.post(
    "http://localhost:8000/token", data={
        "grant_type": "password",
        "username": "lucas",
        "password": "test123",
    }, auth=("client-id", "client-secret"))

# Printing the information for debugging and illustration purposes
print(tokenrequest.text)
# Extracting the token that came with the response
token = tokenrequest.json()["access_token"]

# Using the token in the headers of a secured endpoint
headerswithtoken = {
"accept" : "application/json",
"Authorization": f'Bearer {token}'
}


def test_get_users():
    response = requests.get('http://127.0.0.1:8000/users/', headers=headerswithtoken)
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)

    for user in data:
        assert isinstance(user,dict)
        assert 'id' in user
        assert 'name' in user


def test_get_active_user():
    response = requests.get('http://127.0.0.1:8000/users/me', headers=headerswithtoken)
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, dict)
    assert 'id' in data
    assert 'name' in data
    assert 'is_active' in data

    assert data['is_active'] == True


def test_get_products():
    response = requests.get('http://127.0.0.1:8000/products/', headers=headerswithtoken)
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)

    for product in data:
        assert isinstance(product,dict)
        assert 'id' in product
        assert 'name' in product


def test_get_locations():
    response = requests.get('http://127.0.0.1:8000/locations/', headers=headerswithtoken)
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)

    for location in data:
        assert isinstance(location,dict)
        assert 'id' in location
        assert 'zipcode' in location


def test_create_user():
    new_user = {'name': 'kato', 'password' : 'kato123'}
    response = requests.post('http://127.0.0.1:8000/user/', data=json.dumps(new_user))
    assert response.status_code == 200
    data = response.json()
    assert type(data["name"]) == str
    assert type(data["password"]) == str


def test_create_product():
    new_product = {'name': 'pringles', 'price' : 1.50, 'category': 'chips'}
    response = requests.post('http://127.0.0.1:8000/product/', data=json.dumps(new_product), headers=headerswithtoken)
    assert response.status_code == 200
    data = response.json()
    assert type(data["name"]) == str
    assert type(data["price"]) == float
    assert type(data["category"]) == str


def test_create_location():
    new_location = {'city': 'Vosselaar', 'zipcode' : 2350, 'chief': 'Jonas'}
    response = requests.post('http://127.0.0.1:8000/location/', data=json.dumps(new_location), headers=headerswithtoken)
    assert response.status_code == 200
    data = response.json()
    assert type(data["city"]) == str
    assert type(data["zipcode"]) == int
    assert type(data["chief"]) == str


def test_update_product():
    product_name = 'bugels'
    data = {'name': 'bugels', 'price': 1.30, 'category': 'chips'}
    response = requests.put(f'http://127.0.0.1:8000/product/{product_name}', json=data, headers=headerswithtoken)
    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, dict)
    assert 'name' in data
    assert 'price' in data
    assert 'category' in data
    assert data['name'] == 'bugels'
    assert data['price'] == 1.30
    assert data['category'] == 'chips'


def test_delete_product():
    product_id = '2'
    response = requests.delete(f'http://127.0.0.1:8000/product/{product_id}', headers=headerswithtoken)
    assert response.status_code == 200
    assert response.text == '{"Product removed":true}'
