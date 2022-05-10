def test_get_all_cars_with_empty_db_returns_empty_list(client):
    response = client.get('/cars')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [] 