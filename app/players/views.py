from django.shortcuts import render, redirect
from django.views import View

from utils.test_fortnite_search import getFortnite


class PlayerDetailView(View):

    def get(self, request, *args, **kwargs):
        return redirect('index')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        context = getFortnite(name)
        return render(request, 'result.html', context)
