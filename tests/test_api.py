from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# get product tests
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

def test_product_not_found():
    r = client.get('/api/products/9999')
    assert r.status_code == 404

# review adding successful scenario
def test_add_review_via_post_redirect():
    r = client.post('/product/1/reviews', data={'review': 'Great!', 'rating': 5}, follow_redirects = False)
    assert r.status_code == 303

# Review error tests
def test_add_empty_review_returns_error():
    r = client.post('/product/1/reviews', data={'review': '      '})
    assert r.status_code == 400

def test_add_negative_review_rating_returns_error():
    r = client.post('/product/1/reviews', data={'review': 'text', 'rating': -2})
    assert r.status_code == 400

def test_add_larger_review_rating_returns_error():
    r = client.post('/product/1/reviews', data={'review': 'text', 'rating': 99})
    assert r.status_code == 400

def test_review_text_missing_returns_error():
    r = client.post('/product/1/reviews', data={'rating': 5})
    assert r.status_code == 400

def test_review_rating_missing_returns_error():
    r = client.post('/product/1/reviews', data={'review': 'text'})
    assert r.status_code == 400
