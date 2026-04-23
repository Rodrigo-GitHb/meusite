def test_post_view_returns_hello_world(client):
    response = client.get("/post/")

    assert response.status_code == 200
    assert response.content == b"Hello World"
