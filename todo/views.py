from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from users.models import User
from todo.models import Todo
from todo.serializers import TodoSerializer, TodoCreateSerializer


class TodoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # 할일 등록
    def post(self, request):
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoShow(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # 할일 조회
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user == user:
            todo = Todo.objects.filter(user_id=user_id)
            serializer = TodoSerializer(todo, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class TodoDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # 할일 수정
    def put(self, request, todo_id, user_id):
        user = get_object_or_404(User, id=user_id)
        todo = Todo.objects.get(id=todo_id)
        if request.user == user:
            serializer = TodoCreateSerializer(todo, data=request.data)

            if serializer.is_valid():
                if request.data.get("is_complete") == True:
                    serializer.save(completion_at=timezone.now())
                else:
                    serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_400_BAD_REQUEST)

    # 할일 삭제
    def delete(self, request, todo_id, user_id):
        user = get_object_or_404(User, id=user_id)
        todo = Todo.objects.get(id=todo_id)
        if request.user == user:
            todo.delete()
            return Response("삭제 완료!", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_400_BAD_REQUEST)
