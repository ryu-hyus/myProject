from django.urls import path
from myApp.views import PersonView

app_name = "myApp"

urlpatterns = [
    path('member/', PersonView.as_view(), name='member_list'),
]