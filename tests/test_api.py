import pytest
from app import app, db
from models import Product

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_add_product(client):
    response = client.post('/products', json={
        'name': 'Test Product',
        'description': 'This is a test product',
        'price': 9.99,
        'quantity': 10
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Test Product'

def test_get_products(client):
    client.post('/products', json={
        'name': 'Test Product',
        'description': 'This is a test product',
        'price': 9.99,
        'quantity': 10
    })
    response = client.get('/products')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1

def test_get_product(client):
    client.post('/products', json={
        'name': 'Test Product',
        'description': 'This is a test product',
        'price': 9.99,
        'quantity': 10
    })
    response = client.get('/products/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Test Product'

def test_update_product(client):
    client.post('/products', json={
        'name': 'Test Product',
        'description': 'This is a test product',
        'price': 9.99,
        'quantity': 10
    })
    response = client.put('/products/1', json={
        'name': 'Updated Product',
        'description': 'This is an updated test product',
        'price': 19.99,
        'quantity': 5
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Updated Product'

def test_delete_product(client):
    client.post('/products', json={
        'name': 'Test Product',
        'description': 'This is a test product',
        'price': 9.99,
        'quantity': 10
    })
    response = client.delete('/products/1')
    assert response.status_code == 204
