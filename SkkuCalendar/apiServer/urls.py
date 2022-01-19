from django.urls import path
from . import views

app_name="apiServer"

urlpatterns = [
    path('<int:month>',views.MainView.as_view()),
    path('day/<int:month>/<int:day>',views.DayView.as_view()),
]
