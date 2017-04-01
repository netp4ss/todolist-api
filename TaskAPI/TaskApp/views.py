from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Task
from .Serializers import TaskSerializer
from datetime import datetime


class TaskList(APIView):

    def get_object(self,id):
        try:
            return Task.objects.get(id=id)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request):
        tasks = Task.objects.all()

        qdate = request.GET.get("date")
        if qdate:
            dd = datetime.strptime(qdate, "%Y-%m-%d")
            tasks = Task.objects.filter(date_created__day=dd.day,
                                        date_created__month=dd.month,
                                        date_created__year=dd.year)

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        task = self.get_object(id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        task = self.get_object(id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
