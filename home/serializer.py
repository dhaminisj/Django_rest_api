from rest_framework import serializers
from .models import Todo,TimingTodo
from django.template.defaultfilters import slugify
import re
class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    class Meta :
        model = Todo
        fields = ['user','todo_title','slug','todo_description','is_done','uid']
        # exclude = ['created_at']


    def get_slug(self,obj):
        return slugify(obj.todo_title)
    

    def validate_todo_title(self,data):
        if data :
            todo_title = data
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

            if len(todo_title)<3:
                raise serializers.ValidationError('todo title must be more than 3 characters')

            if not regex.search(todo_title) == None:
                raise serializers.ValidationError('todo_title cannot contain special characters')
        return data  
    # def validate(self,validated_data):
    #     print(validated_data)
    #     if validated_data.get('todo_title'):
    #         todo_title = validated_data['todo_title']
    #         regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    #         if len(todo_title)<3:
    #             raise serializers.ValidationError('todo title must be more than 3 characters')

    #         if not regex.search(todo_title) == None:
    #             raise serializers.ValidationError('todo_title cannot contain special characters')
            
            
        # return validated_data


class TimingTodoSerializer(serializers.ModelSerializer):
     todo = TodoSerializer()
     class Meta  :
         model = TimingTodo
         exclude = ['created_at','updated_at']
        #  depth = 1
         def create(self, validated_data):
             return Todo.objects.create(**validated_data)