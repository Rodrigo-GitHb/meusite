from django.shortcuts import render


def post_view(request):
    return render(request, "blog/index.html")
