import json
from typing import Any, Dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from myApp.models import Member
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(csrf_exempt, name="dispatch")
class PersonView(View):
    #조회
    def get(self, request, pk=None):
        #단건조회
        if pk is not None:

            member = Member.objects.filter(id=pk).values().first()

            if not member:
                return JsonResponse({"error": "Person not found"}, status=404)
            return JsonResponse(member)
        # 다건조회
        else:
            members = Member.objects.all().values()
            return JsonResponse(list(members) , safe=False)
    
    # 수정
    def put(self, request, pk):
        person = get_object_or_404(Member, pk=pk)
        data = json.loads(request.body)

        person.age = data.get("age") or person.age
        person.firstname = data.get("firstname") or person.first_name
        person.lastname = data.get("lastname") or person.last_name

        person.save()
        return JsonResponse(data)


    # 삭제
    def delete(self, request, pk):
        person = get_object_or_404(Member, pk=pk)
        person.delete()
        return HttpResponse(status=200)

    # 등록
    def post(self, request):
        data = json.loads(request.body)

        p = Member(
            firstname=data.get("firstname"),
            lastname=data.get("lastname"),
            age=data.get("age"),
        )
        p.save()
        return HttpResponse(status=200)
    
class HelloTemplateView(TemplateView):
    template_name = "hello.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["my_name"] = "류현승"

        return context

class MemberTemplateView(TemplateView):
    template_name = "member.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["my_name"] = "류현승"

        member = Member.objects.filter(id =3).values().first()
        context["member"] = member
        
        return context
    
class JqueryTemplateView(TemplateView):
    template_name = "jquery_study.html"
    
class MemberListTemplateView(TemplateView):
    template_name = "member_list.html"
