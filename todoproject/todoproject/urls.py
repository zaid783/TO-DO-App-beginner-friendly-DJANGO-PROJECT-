from django.contrib import admin
from django.urls import path
from todoapp.views import todoappview, addtoview, deletetoview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp/', todoappview),
    path('addTodoItem/', addtoview),
    path('deleteTodoItem/<int:i>/', deletetoview),
]
