from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/',about, name='about'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:cat_slug>/', show_category, name='category'),
]
