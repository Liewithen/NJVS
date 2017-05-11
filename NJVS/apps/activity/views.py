from django.shortcuts import render
from datetime import datetime, date
from django.views.generic import View
from models import Activity
# Create your views here.

# def selectActivity(acts):
#     d = date.today()
#     temp = [[],[],[],[],[],[],[]]
#     for act in acts:
#         for day in range(0, 7):
#             if  d + datetime.timedelta(days=day) >=  act.start_time and d + datetime.timedelta(days=day) <=  act.end_time :
#                 temp[day].append(act)
#             else :
#                 break
#     for t in temp:
#         print t
#     return temp


class ActivityView(View):
    def get(self, request):
        # d = datetime.today()
        # acts = Activity.objects.filter(end_time__gte = d).order_by('end_time')
        # selectActivity(acts)
        return render(request, 'activity/activity.html', {})


class ActProfileView(View):
    def get(self, request):
        return render(request, 'activity/actprofile.html', {})