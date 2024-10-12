from django.http import HttpResponse
from django.template import loader

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /accounts/login/",
        "Disallow: /accounts/logout/",
        "Disallow: /accounts/register/",
        "Allow: /",
        "",
        "Sitemap: https://www.artbykita.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")