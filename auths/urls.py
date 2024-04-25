from django.urls import path
from .import views

app_name = 'auths'

urlpatterns = [
    path('signup/',views.signup_view,name='signup'),
    path('sign-in/',views.login_view,name='sign-in'),
]