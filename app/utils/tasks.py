# from celery import shared_task
# from djoser.conf import settings
# from users.models import User

# @shared_task
# def send_verify_email(to, user_id):
#     user = User.objects.get(pk=user_id)
#     context = {'user': user}
#     settings.EMAIL.activation(context=context).send(to)

# @shared_task
# def send_confirm_email(to, user_id):
#     user = User.objects.get(pk=user_id)
#     context = {'user': user}
#     settings.EMAIL.confirmation(context=context).send(to)

# @shared_task
# def send_password_reset_email(user_id):
#     user = User.objects.get(pk=user_id)
#     context = {'user': user}
#     to = [user.email]
#     settings.EMAIL.password_reset(context=context).send(to)

# @shared_task
# def partner_send_password_reset_email(user_id):
#     user = User.objects.get(pk=user_id)
#     context = {'user': user}
#     to = [user.email]
#     settings.EMAIL.partner_password_reset(context=context).send(to)