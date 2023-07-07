from django.urls import path
from myApp.views import PersonView
from myApp.views import HelloTemplateView
from myApp.views import MemberTemplateView
from myApp.views import JqueryTemplateView, MemberListTemplateView, MemberDetailTemplateView

app_name = "myApp"

urlpatterns = [
    path('member/', PersonView.as_view(), name='member_list_create'),
    path('member/<int:pk>/', PersonView.as_view(), name='member_detail_update_delete'),
    path("hello/", HelloTemplateView.as_view(), name='hello_template_view'),
    path("memberinfo/", MemberTemplateView.as_view(), name='member_template_view'),
    path("jquery/", JqueryTemplateView.as_view(), name='jquery_template_view'),
    path("memberlist/", MemberListTemplateView.as_view(), name='memlist_template_view'),
    path("memberdetail/", MemberDetailTemplateView.as_view(), name='memdetail_template_view')
]