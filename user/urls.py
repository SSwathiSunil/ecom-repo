from django.urls import path
from django.urls.conf import include
from.import views

app_name='user'

urlpatterns=[
    path('',views.Index),
    path('userr',views.New)
]