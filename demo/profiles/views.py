from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from userena.views import profile_detail as __profile_detail


def profile_detail(request, username):
    view_user = get_object_or_404(User, username=username)
    return __profile_detail(request, username,)
