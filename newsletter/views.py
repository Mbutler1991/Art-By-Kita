import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import NewsletterSignupForm
from .models import NewsletterSubscriber


def send_newsletter(subject, content, email):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    sender = {"name": "Art By Kita", "email": "kita@artbykita.com"}
    to = [{"email": email}]
    html_content = f"<html><body><p>{content}</p></body></html>"

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


def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Check if email already exists
            if NewsletterSubscriber.objects.filter(email=email).exists():
                messages.error(request, "This email is already subscribed.")
            else:
                NewsletterSubscriber.objects.create(email=email)

                subject = "Welcome to Our Newsletter!"
                content = "Thank you for subscribing to our newsletter. Stay tuned for updates!"
                send_newsletter(subject, content, email)

                return redirect('newsletter:newsletter_thankyou')
    else:
        form = NewsletterSignupForm()

    return render(request, 'newsletter/newsletter_signup.html', {'form': form})


def newsletter_thankyou(request):
    return render(request, 'newsletter/newsletter_thankyou.html')
