from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import NewsletterSignupForm
from .emails import send_newsletter
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from . import settings

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
    def send_newsletter(subject, content, email):
    # Configure API key authorization: api-key
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key['api-key'] = settings.BREVO_API_KEY 

    # Create an instance of the API class
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    
        sender = {"name": "Art By Kita", "email": "your_email@domain.com"}  
        to = [{"email": email}]  
        html_content = f"<html><body><p>{content}</p></body></html>"  

        subject = subject  
    
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
            to=to,
            sender=sender,
            subject=subject,
            html_content=html_content
        )

        try:
            api_response = api_instance.send_transac_email(send_smtp_email)
            print(f"Newsletter sent successfully to {email}")
        except ApiException as e:
            print(f"Failed to send newsletter: {e}")

def newsletterthank_you(request):
    return render(request, 'newsletter_thankyou.html')