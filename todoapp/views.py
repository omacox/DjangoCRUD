from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.http import HttpResponse


def todoproject(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect back to the same page after adding
            return redirect('todoproject_url')
    else:
        form = TodoForm()

    todos = Todo.objects.all()  # Get all todos to display
    return render(request, 'todoapp/todo.html', {
        'form': form,
        'todos': todos
    })


def createTodoView(request):
    form = TodoForm
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = "todoapp/todo.html"
    context = {"form": form}
    return render(request, template_name, context)


def showTodoView(request):
    obj = Todo.objects.all()
    template_name = "todoapp/show.html"
    context = {"obj": obj}
    return render(request, template_name, context)


def updateTodoView(request, f_id):
    obj = Todo.objects.get(id=f_id)
    form = TodoForm(instance=obj)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = "todoapp/todo.html"
    context = {"form": form}
    return render(request, template_name, context)


def deleteTodoView(request, f_id):
    obj = Todo.objects.get(id=f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    template_name = "todoapp/confirmation.html"
    context = {"obj": obj}
    return render(request, template_name, context)
