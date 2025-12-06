from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_products():
    r = client.get('/api/products')
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_get_product_detail():
    r = client.get('/api/products/1')
    assert r.status_code == 200
    data = r.json()
    assert data['id'] == 1
    assert 'name' in data

def test_add_review_via_post_redirect():
    r = client.post('/product/1/reviews', data={'review': 'Great!'}, follow_redirects = False)
    assert r.status_code == 303

def test_add_short_review_returns_error():
    r = client.post('/product/1/reviews', data={'review': 'ok'})
    assert r.status_code == 200
    assert 'error' in r.json()
