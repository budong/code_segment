# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response
from coltrane.models import Category
from django.views.generic.list_detail import object_list
from django.contrib.auth.models import User
from graduate.accounts.models import MyProfile
from django.views.generic.list_detail import object_list


import sys
reload( sys )
sys.setdefaultencoding('utf-8')

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return object_list(request, queryset=category.live_entry_set(), extra_context={
        'category': category
    })


def recommend_article(request):
    #找出用户浏览次数最多的一个标签
    user_object = get_object_or_404(User, username=request.user)
    userena_object = get_object_or_404(MyProfile, user=user_object.id)
    max_num = max(userena_object.network,userena_object.system,userena_object.database,userena_object.other)
    if userena_object.network == max_num:
        category = 'network'
    elif userena_object.system == max_num:
        category = 'system'
    elif userena_object.database == max_num:
        category = 'database'
    elif userena_object.other == max_num:
        category = 'database'
    #找到相应标签对应的所有文章对象
    category_object = Category.objects.get(title=category)
    queryset = category_object.entry_set.all()
    return object_list(request,queryset)
    
