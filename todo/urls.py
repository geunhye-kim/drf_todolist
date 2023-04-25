from django.urls import path
from todo import views


urlpatterns = [
    path('', views.TodoView.as_view(), name='todo_view'),
    path('<int:user_id>/',
         views.TodoShow.as_view(), name='todo_detail_view'),
    path('<int:user_id>/<int:todo_id>/',
         views.TodoDetailView.as_view(), name='todo_delete_view'),
]
