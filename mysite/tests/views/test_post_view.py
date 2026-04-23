def test_post_view_returns_hello_world(client):
    response = client.get("/post/")

    assert response.status_code == 200
    assert b"Hello World" in response.content
    template_names = [template.name for template in response.templates if template.name]
    assert "blog/index.html" in template_names
