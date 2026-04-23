from django.contrib.admin.sites import site

from blog.models import Post


def test_post_model_is_registered_in_admin():
    assert site.is_registered(Post)
