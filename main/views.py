
# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from django.forms.models import model_to_dict
import json
# Create your views here.
def index(request):
  buil_list = []
  buildings = Building.objects.all()
  for building in buildings:
    buil_dict = model_to_dict(building)
    buil_list.append(buil_dict)
  patient_num = School_Find.objects.last()
  employee = patient_num.employee
  st = patient_num.schoolteacher
  underg = patient_num.underg
  postg= patient_num.postg
  all = employee + st + underg + postg
  date = patient_num.date
  info = Info.objects.all()
  return render(request, 'main/index.html', {'buil_list':buil_list, 'employee':employee, 'st':st, 'underg':underg,
                                              'postg':postg, 'all':all, 'date':date, 'info':info,
                                             })