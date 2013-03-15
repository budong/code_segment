# Create your views here.
from django.shortcuts import get_object_or_404
from graduate.accounts.models import MyProfile

def my_view():
    my_object = get_object_or_404(MyProfile, pk=1)
    return my_object.increase_network_num()
