from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer,TimingTodoSerializer
from .models import Todo,TimingTodo
from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework.decorators import action
from django.core.paginator import Paginator
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .helpers import paginate
@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
            'message': 'Django running',
            'method_called': 'You called Get method'
        })
    elif request.method == 'POST':
        return Response({
            'status': 200,
            'message': 'Django running',
            'method_called': 'You called Post method'
        })
    elif request.method == 'PATCH':
        return Response({
            'status': 200,
            'message': 'Django running',
            'method_called': 'You called Patch method'
        })
    elif request.method == 'PUT':
        return Response({
            'status': 200,
            'message': 'Django running',
            'method_called': 'You called Put method'
        })
    else:
        return Response({
            'status': 400,
            'message': 'Invalid request',
            'method_called': 'You called an invalid method'
        })


@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer(todo_objs,many = True)
    return Response ({
        'status':True,
        'message':'Todo fected',
        'data':serializer.data
    })

@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({
            'status':True,
            'message':"success data",
            "data":serializer.data
        })
        return Response({
            'status':False,
            'message':"invalid data",
            "data":serializer.errors
        })
   

    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'message': 'Something went wrong',
    })
    # TodoSerializer


@api_view(['PATCH'])
def patch_todo(request):
    try:
         data = request.data
         if not data.get('uid'):
            return Response({
                'status':False,
                'message':'uid is required',
                'data':{}
            })
         obj = Todo.objects.get(uid= data.get('uid'))
         serializer = TodoSerializer(obj,data = data, partial = True)
         if serializer.is_valid():
            serializer.save()
            return Response({
            'status':True,
            'message':"success data",
            "data":serializer.data
            })
         return Response({
            'status':False,
            'message':"invalid data",
            "data":serializer.errors
        })
    
    except Exception as e :
        print(e)
    return Response({
        'status':False,
        'message':'invalid uid',
        'data':{}
    })


class TodoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        todo_objs = Todo.objects.filter(user = request.user)
        page = request.GET.get('page',1)
        page_obj = Paginator(todo_objs, page)
        results = paginate(todo_objs,page_obj,page)
        serializer = TodoSerializer(results['results'],many = True)
        return Response ({
        'status':True,
        'message':'Todo fected',
        'data':{'data':serializer.data,'pagination':results['pagination']}
    })
    def post(self,request):
        try:
            data = request.data
            data['user'] = request.user.id
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
                return Response({
            'status':True,
            'message':"success data",
            "data":serializer.data
        })
            
            return Response({
            'status':False,
            'message':"invalid data",
            "data":serializer.errors
        })
   

        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'message': 'Something went wrong',
    })
    def patch(self,request):
        return Response({
            'status': 200,
            'message': 'Django running',
            'method_called': 'You called patch method'
        })
    def put(self,request):
         return Response({
            'status': 200,
            'message': 'Django running',
            'method_called': 'You called put method'
        })
    def delete(self,request):
         return Response({
            'status': 200,
            'message': 'Django running',
            'method_called': 'You called delete method'
        })


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    @action(detail=False, methods=['GET'])
    def get_timing_todo(self,request):
        objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(objs,many = True)
        return Response({
            'status':True,
            'message':'timing todo feteched',
            'data':serializer.data
        })


    @action(detail=True, methods=['post'])
    def add_date_to_todo(self,request):
        try :
            data = request.data
            serializer = TimingTodoSerializer(data= data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':True,
                    'message':'success data',
                    'data':serializer.data
                })
            
            return Response({
            'status':False,
            'message':"invalid data",
            "data":serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': 'Something went wrong',
            })

