from django.urls import path
from . import views

app_name="apiServer"

urlpatterns = [
    path('post',views.MainView.as_view()),
    path('<int:month>',views.MainView.as_view()),
    path('detail/<int:month>/<int:day>',views.DayView.as_view()),
    path('detail/<int:id>',views.PutView.as_view()),
]
