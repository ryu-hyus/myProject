from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from myApp.models import Member


class PersonView(View):

    def get(self, request):
        people = Member.objects.all()
        return JsonResponse({"data": list(people.values())})
