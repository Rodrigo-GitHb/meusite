import pytest
from django.contrib.admin.sites import site
from django.urls import reverse

from django.contrib.auth.models import User

from blog.models import Post


def test_post_model_is_registered_in_admin():
    assert site.is_registered(Post)


@pytest.mark.django_db
def test_post_admin_add_page_is_accessible(client):
    User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="admin123",
    )
    client.login(username="admin", password="admin123")

    response = client.get(reverse("admin:blog_post_add"))

    assert response.status_code == 200
