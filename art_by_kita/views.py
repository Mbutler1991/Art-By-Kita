from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import NewsletterSignupForm
from .emails import send_newsletter

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

def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = "Welcome to Our Newsletter!"
            content = "Thank you for subscribing to our newsletter. Stay tuned for updates!"
            send_newsletter(subject, content, email)
            return redirect('newsletter_thankyou')  
    else:
        form = NewsletterSignupForm()
    return render(request, 'newsletter_signup.html', {'form': form})

def thank_you(request):
    return render(request, 'newsletter_thankyou.html')