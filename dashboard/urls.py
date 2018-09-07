from django.urls import path
from django.conf.urls import url

from dashboard.views import DashboardView

urlpatterns =[
    url(r'^$', DashboardView.as_view()),
]