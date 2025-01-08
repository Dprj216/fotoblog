from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from authentication.views import login_page

urlpatterns = [
    path('', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
