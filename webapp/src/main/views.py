from celery.result import AsyncResult
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from main import tasks
from main.tasks import cpu_task


def home(request):
    tasks.download_a_cat.delay()
    return HttpResponse('<h1>Гружу кота!</h1>')


class TaskSetter(APIView):
    def get(self, request, formant=None):
        res = cpu_task.delay()
        return Response(res.id)
