from django.conf.urls import url
from login.forms import LoginForm
from django.contrib.auth import views as auth_views
from login.views import UserCreateView

app_name = "authentication"

urlpatterns =[
    url(r'^$', auth_views.LoginView.as_view(template_name="system/login.html", authentication_form=LoginForm), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name="logout"),
    url(r'^register/$', UserCreateView.as_view(), name="register"),
]