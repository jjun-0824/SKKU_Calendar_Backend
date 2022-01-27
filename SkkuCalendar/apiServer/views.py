
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ScheduleSerializer
from .models import PostSchedule
import datetime
from django.db.models import Q
from django.http.response import JsonResponse

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
            monthSchedule = PostSchedule.objects.filter(
                Q(start_date__gte=start,start_date__lte=end)|
                Q(end_date__gte=start,end_date__lte=end)|
                Q(start_date__gte=start,end_date__lte=end)
            )
            monthSchedule_serializer = ScheduleSerializer(monthSchedule,many=True)
            return Response(monthSchedule_serializer.data, status="200")
        
    def post(self,request):
        post_serializer = ScheduleSerializer(data=request.data)
        
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
class PutView(APIView):       
    def put(self, request,id):
        try: 
            update_post = PostSchedule.objects.get(post_id=id) 
        except PostSchedule.DoesNotExist: 
            return JsonResponse({'message': 'The post does  not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
        update_serializer = ScheduleSerializer(update_post,data=request.data)    
        
        if update_serializer.is_valid(): 
            update_serializer.save() 
            return JsonResponse(update_serializer.data) 
        else:
            return JsonResponse(update_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    def delete(self, request, id):
        try: 
            delete_post = PostSchedule.objects.get(post_id=id) 
        except PostSchedule.DoesNotExist: 
            return JsonResponse({'message': 'The post does  not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
        delete_post= PostSchedule.objects.get(post_id=id)
        delete_post.delete()
        
        return JsonResponse({'message': 'post was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    
#day
class DayView(APIView):
    def get (self,request,month,day):
        select_date = datetime.date(2022,month,day)
        # start_date<= select_date <= end_date
        daySchedule = PostSchedule.objects.filter(end_date__gte= select_date, start_date__lte = select_date)
        daySchedule_serializer = ScheduleSerializer(daySchedule,many=True)
        
        return Response(daySchedule_serializer.data,status="200")
        