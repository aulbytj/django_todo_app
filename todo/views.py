from django.shortcuts import render
from .models import Todo

# Create your views here.


#  CRUD CREATE READ UPDATE DELETE



# CREATE VIEW



# READ VIEW
def todo_list(request):
  todos = Todo.objects.all()
  context = {'todos': todos}
  return render(request, 'todo/todo_list.html', context)


# UPDATE VIEW



# DELETE VIEW