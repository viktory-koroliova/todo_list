from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View

from todo_list.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:task-list")
    queryset = Task.objects.prefetch_related("tags")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")


# def change_is_done_status(request: HttpRequest, pk: int) -> HttpResponseRedirect:
#     task = Task.objects.get(id=pk)
#     task.is_done = not task.is_done
#     task.save()
#     return HttpResponseRedirect(reverse_lazy("todo_list:task-list"))

class IsDoneUpdateView(View):
    def post(self, request: HttpRequest, pk: int) -> redirect:
        task = Task.objects.get(id=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("todo_list:task-list")

    def get(self, request: HttpRequest, **kwargs) -> redirect:
        return redirect("todo_list:task-list")
