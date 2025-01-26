from users.models import User
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


def reset_password(email):
    """Сбрасывает пароль для входа в приложение"""
    users = User.objects.all()
    email_list = []

    for user in users:
        email_list.append(user.email)

    if email in email_list:
        user = User.objects.filter(email=email)
        uid = user.id

        send_mail(
            subject="Подтверждение почты",
            message=f"Привет! Пройди поссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )