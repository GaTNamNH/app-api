import hashlib
from urllib.request import urlopen

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
# from utils.tasks import send_verify_email


def auto_logout(*args, **kwargs):
    """Do not compare current user with new one"""
    return {'user': None}


# def save_avatar(strategy, details, user=None, *args, **kwargs):
#     """Get user avatar from social provider."""
#     if user:
#         backend_name = kwargs['backend'].__class__.__name__.lower()
#         response = kwargs.get('response', {})
#         social_thumb = None
#         if 'facebook' in backend_name:
#             if 'id' in response:
#                 social_thumb = (
#                     'http://graph.facebook.com/{0}/picture?type=normal'
#                 ).format(response['id'])
#         elif 'twitter' in backend_name and response.get('profile_image_url'):
#             social_thumb = response['profile_image_url']
#         elif 'googleoauth2' in backend_name and response.get('image', {}).get('url'):
#             social_thumb = response['image']['url'].split('?')[0]
#         else:
#             social_thumb = 'http://www.gravatar.com/avatar/'
#             social_thumb += hashlib.md5(user.email.lower().encode('utf8')).hexdigest()
#             social_thumb += '?size=256'
#         if social_thumb and not user.profile_image:
#             img_temp = NamedTemporaryFile(delete=True)
#             img_temp.write(urlopen(social_thumb).read())
#             img_temp.flush()
#             user.profile_image.save(f"image_{user.pk}", File(img_temp))
#         strategy.storage.user.changed(user)


# def check_for_email(backend, uid, user=None, *args, **kwargs):
#     if not kwargs['details'].get('email') or '@' not in kwargs['details'].get('email'):
#         kwargs['details']['email'] = None

# raise CustomException(code='not_verified_email', detail={'error': "Email wasn't provided by oauth provider"})
USER_FIELDS = ['username', 'email']


def create_user(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    fields = dict((name, kwargs.get(name, details.get(name)))
                  for name in backend.setting('USER_FIELDS', USER_FIELDS))
    if not fields:
        return

    user = strategy.create_user(**fields)
    # if user.email:
    #     send_verify_email.delay([user.email], user.id)
    return {
        'is_new': True,
        'user': user
    }
