from django.shortcuts import render
from django.conf.urls import url
from django.views.generic import View
from my_lab6.models import ComputerModel

class ComputerView(View):
    def get(self, request):
        computers = ComputerModel.objects.all()
        return  render(request, 'computer.html', {'computers':computers})

