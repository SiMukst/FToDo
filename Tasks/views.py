from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.utils import timezone

# Constant
TODAY = timezone.now().date()
DAILY_LIMIT = 4

# Create your views here.
def index(request):
    task_list = Task.objects.filter(date_created__contains=TODAY)
    incomplete_task_list = task_list.filter(is_done=False)
    complete_task_list = task_list.filter(is_done=True)
    
    has_task = task_list.exists()
    has_incomplete_tasks = incomplete_task_list.exists()
    
    context = {
        'incomplete_tasks': incomplete_task_list,
        'complete_tasks': complete_task_list,
        'completed': not has_incomplete_tasks,
        'has_task': has_task,
    }
    
    return render(request, 'index.html', context)

def add_task(request):
    if request.method == "POST":
        taskname = request.POST.get('taskname')
        
        if taskname:
            task_list = Task.objects.filter(date_created__contains=TODAY)
            incomplete_task_list = task_list.filter(is_done=False)
            complete_task_list = task_list.filter(is_done=True)
            
            daily_count = task_list.count()
            has_task = task_list.exists()
            has_incomplete_tasks = incomplete_task_list.exists()
            
            if daily_count >= DAILY_LIMIT:
                context = {
                    'incomplete_tasks': incomplete_task_list,
                    'complete_tasks': complete_task_list,
                    'completed': not has_incomplete_tasks,
                    'has_task': has_task,
                    'limit_reached': "Let's focus to only 4 tasks per day",
                }
                return render(request, 'index.html', context)
            else:
                task, created = Task.objects.get_or_create(taskname=taskname)
                return redirect('Tasks:index')
    
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('Tasks:index')

def mark_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == "POST":
        task.is_done = True # Mark as done
        task.save()
        
        return redirect('Tasks:index')
    
    else:
        return redirect('Tasks:index')