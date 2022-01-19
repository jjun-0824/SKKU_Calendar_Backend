
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ScheduleSerializer
from .models import Schedule
import datetime
from django.db.models import Q

# month
class MainView(APIView):
    def get(self,request,month):
            start = datetime.date(2022, month, 1)
            if (month <12) :
                end = datetime.date(2022, month+1 , 1)
            else :
                end = datetime.date(2023, 1 , 1) #연도는 수동변경 필요
        # 1. start<= start_date <= end
        # 2. start <= end_date <= end
        # 3. start <=start_date , end>= end_date
            monthSchedule_queryset = Schedule.objects.filter(
                Q(start_date__gte=start,start_date__lte=end)|
                Q(end_date__gte=start,end_date__lte=end)|
                Q(start_date__gte=start,end_date__lte=end)
            )
            monthSchedule_queryset_serializer = ScheduleSerializer(monthSchedule_queryset,many=True)
            return Response(monthSchedule_queryset_serializer.data, status="200")
        
    def post(self,request):
        post_queryset_serializer = ScheduleSerializer(data=request.data)
        
        if post_queryset_serializer.is_valid():
            post_queryset_serializer.save()
            return Response(post_queryset_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(post_queryset_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#day
class DayView(APIView):
    def get (self,request,month,day):
        select_date = datetime.date(2022,month,day)
        # start_date<= select_date <= end_date
        daySchedule_queryset = Schedule.objects.filter(end_date__gte= select_date, start_date__lte = select_date)
        daySchedule_queryset_serializer = ScheduleSerializer(daySchedule_queryset,many=True)
        
        return Response(daySchedule_queryset_serializer.data,status="200")
        