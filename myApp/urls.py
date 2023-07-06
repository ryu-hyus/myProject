from django.urls import path
from myApp.views import PersonView
from myApp.views import HelloTemplateView

app_name = "myApp"

urlpatterns = [
    path('member/', PersonView.as_view(), name='member_list_create'),
    path('member/<int:pk>/', PersonView.as_view(), name='member_detail_update_delete'),
    path("hello/", HelloTemplateView.as_view(), name='hello_template_view')
]