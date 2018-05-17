from django.views.generic import View
from django.shortcuts import render


class myResumeView(View):
    def get(self, request):
        return render(request,'static/myresume.html')

