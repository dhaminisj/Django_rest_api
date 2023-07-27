from django.urls import path
from .views import home,post_todo,get_todo,patch_todo,TodoView,TodoViewSet # import the view you just created
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'todo-view-set',TodoViewSet,basename="todo")


urlpatterns = [
    path('', home, name='home'),  
    # map the root URL of this app ('') to the home view
    path('post-todo/',post_todo,name ='post_todo'),
    path('get-todo/',get_todo,name = 'get_todo'),
    path('patch-todo/',patch_todo,name='patch_todo'),
    path('todo/',TodoView.as_view()),
]

urlpatterns += router.urls