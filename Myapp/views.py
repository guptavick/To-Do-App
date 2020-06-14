from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect

from .models import Todo

# Create your views here.

def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request,'Myapp/index.html',{'todo_items':todo_items})

def add_todo(request):
    added_date = timezone.now()
    content = request.POST['item']
    Todo.objects.create(added_date = added_date, text = content)
    return HttpResponseRedirect('/Mytodos')

def delete_todo(request, todo_id):
    Todo.objects.get(id = todo_id).delete()
    return HttpResponseRedirect('/Mytodos')

def filter_by_date(request):
    date = request.POST['date']
    todo_items = Todo.objects.filter(added_date__contains = date)
    return render(request,'Myapp/filter.html',{'todo_items':todo_items})


