from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Task

from typing import Optional


def validate_signup_fields(username: str, email: str, pswd1: str, pswd2: str) -> Optional[str]:
    if not username:
        return 'Username field is empty'
    elif not username.isalnum():
        return 'Username can consist of alphabets and digits only'
    elif User.objects.filter(username=username):
        return 'Username already exists'
    elif not email:
        return 'Email field is empty'
    elif User.objects.filter(email=email):
        return 'Email already exists'
    elif not pswd1:
        return 'Password field is empty'
    elif not pswd2:
        return 'Confirm password field is empty'
    elif pswd1 != pswd2:
        return 'Passwords don\'t matches'


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pswd2 = request.POST.get('pswd1')
        pswd1 = request.POST.get('pswd2')
        msg = validate_signup_fields(username, email, pswd1, pswd2)

        if msg is None:
            user = User(username=username, email=email)
            user.set_password(pswd1)
            user.is_active = True
            user.save()
            messages.success(request, 'Sucessful signup')
            return render(request, 'registration/signin.html')

        messages.warning(request, msg)

    return render(request, 'registration/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pswd = request.POST.get('pswd')

        user = authenticate(request, username=username, password=pswd)
        if user is None:
            messages.error(request, 'Invalid credentials')
        else:
            login(request, user)
            return redirect(reverse('todo:index'), request=request)

    return render(request, 'registration/signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'Successful signout')
    return redirect(reverse('todo:index'), request=request)


def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'todo/tasks.html', {'tasks': tasks})

    return render(request, 'todo/index.html')


@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')

        if not title:
            messages.info(request, 'Title is empty')
            return render(request, 'todo/create.html')

        try:
            task = Task(user=request.user, title=title, description=desc)
        except Exception as e:
            messages.error(request, e)
            return render(request, 'todo/create.html')
        else:
            task.save()

        return redirect(reverse('todo:index'), request=request)

    return render(request, 'todo/create.html')


@login_required
def search_task(request):
    context = {'is_search': True}

    text = request.GET.get('search').strip()
    tasks = Task.objects.filter(title__contains=text)
    context['tasks'] = tasks

    if text:
        count = len(tasks)
        msg = f'{count} tasks matched the search' if count>1 else f'{count if count==1 else "no"} task matched the search'
        context['search_text'] = text
        messages.info(request, msg)

    return render(request, 'todo/tasks.html', context)


@login_required
def update_task(request, id: int):
    context = {}

    if request.method == 'POST':

        title = request.POST.get('title')
        desc = request.POST.get('description')
        is_finished = request.POST.get('is_finished') == 'on'

        if not title:
            messages.info(request, 'Title is empty')
            return render(request, 'todo/update.html', context)

        else:
            try:
                task = Task.objects.get(id=id)
            except Exception as e:
                messages.error(request, e)
                return render(request, 'todo/update.html', context)
            else:
                task.title = title
                task.description = desc
                task.is_finished = is_finished
                task.save()
            messages.success(request, 'Task successfully updated')
            return redirect(reverse('todo:index'), request=request, context=context)

    task = Task.objects.get(id=id)
    context['task'] = task
    return render(request, 'todo/update.html', context)


@login_required
def delete_task(request, id: int):
    if request.method == 'POST':
        try:
            task = Task.objects.get(id=id)
        except Exception as e:
            messages.error(request, e)
            return render(request, 'todo/create.html')
        else:
            task.delete()

        messages.success(request, 'Task successfully deleted')
        return redirect(reverse('todo:index'), request=request)

    task = Task.objects.get(id=id)
    return render(request, 'todo/delete.html', {'task': task})
