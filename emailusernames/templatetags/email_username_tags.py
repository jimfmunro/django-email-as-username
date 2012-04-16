from django import template

from django.contrib.auth.models import User
from emailusernames.utils import get_user_hash

register = template.Library()

@register.simple_tag
def user_hash(user):
    return get_user_hash(user.username)
