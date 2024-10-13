import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from django.conf import settings

def send_newsletter(subject, content, recipient_email):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    sender = {"name": "Your Website", "email": "your-email@example.com"}
    to = [{"email": recipient_email}]
    subject = subject
    html_content = f"<html><body>{content}</body></html>"

    email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        sender=sender,
        subject=subject,
        html_content=html_content
    )

    try:
        api_response = api_instance.send_transac_email(email)
        print(f"Email sent successfully: {api_response}")
    except ApiException as e:
        print(f"Error sending email: {e}")