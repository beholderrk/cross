from django import forms
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db import models
from main.models import Stat
import json


def index(request):
    return render(request, 'index.html')


class StatForm(forms.ModelForm):
    class Meta:
        model = Stat
        fields = ('leader', 'goodsense', 'freeart', 'trust')

    def save(self, request, commit=True):
        stat = Stat.objects.today().filter(session=request.session.session_key).first()
        if stat:
            cd = self.cleaned_data
            stat.leader = cd['leader']
            stat.goodsense = cd['goodsense']
            stat.freeart = cd['freeart']
            stat.trust = cd['trust']
            self.instance = stat
        stat = super(StatForm, self).save(commit=False)
        stat.session = request.session.session_key or ''
        if commit:
            stat.save()
        return stat

@csrf_exempt
@require_http_methods(["POST"])
def post_stat(request):
    data = json.loads(request.read())
    data['session'] = request.session.session_key
    form = StatForm(data)
    if form.is_valid():
        form.save(request)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': form.errors})


def get_stat(request):
    data = Stat.objects.today().aggregate(
        leader=models.Avg('leader'), goodsense=models.Avg('goodsense'),
        freeart=models.Avg('freeart'), trust=models.Avg('trust'), count=models.Count('id'))
    # data['leader'] = round(data['leader'])
    # data['goodsense'] = round(data['goodsense'])
    # data['freeart'] = round(data['freeart'])
    # data['trust'] = round(data['trust'])
    return JsonResponse(data)