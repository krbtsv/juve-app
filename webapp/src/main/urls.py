from django.urls import path

from main.views import TaskSetter, TaskGetter

urlpatterns = [
    path('settask/', TaskSetter.as_view()),
    path('gettask/', TaskGetter.as_view()),
]
