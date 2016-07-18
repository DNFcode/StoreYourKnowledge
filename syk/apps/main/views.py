from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from .forms import GoalForm, BookForm, NoteForm, CodeExampleForm, TaskForm
from .models import Goal, Book, Note, CodeExample, Task
from syk.apps.main.views_utils import GoalPermissionMixin
from syk.apps.main.views_utils import BaseGoalChildCreateView, BaseGoalChildDeleteView, BaseGoalChildUpdateView, \
    BaseGoalChildListView, BaseGoalChildDetailView, SuccessUrlKwargsMixin, calculate_goal_progress


# goals views
class HomeView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        if self.queryset is None:
            return Goal.objects.filter(owner=self.request.user)
        else:
            return super(HomeView, self).get_queryset()

    def get_context_data(self, **kwargs):
        """
        adding to context progress for goals
        """
        goals = self.get_queryset().prefetch_related('task_set')
        progress = {}

        for goal in goals:
            progress[goal.pk] = calculate_goal_progress(goal.task_set.all())

        kwargs.update({'progress': progress})
        return super(HomeView, self).get_context_data(**kwargs)


class GoalView(GoalPermissionMixin, DetailView):
    template_name = 'goals/goal.html'
    model = Goal
    pk_url_kwarg = 'goal_pk'

    def get_context_data(self, **kwargs):
        goal_id = self.kwargs['goal_pk']
        context = {
            'books': Book.objects.filter(goal_id=goal_id),
            'tasks': Task.objects.filter(goal_id=goal_id),
            'codes': CodeExample.objects.filter(goal_id=goal_id)
        }
        context['progress'] = calculate_goal_progress(context['tasks'])

        context.update(kwargs)
        return super(GoalView, self).get_context_data(**context)


class GoalCreateView(CreateView):
    success_url = reverse_lazy('main:home')
    prefix = 'goal'
    form_class = GoalForm
    model = Goal
    template_name = 'goals/goal_create_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(GoalCreateView, self).form_valid(form)


class GoalUpdateView(GoalPermissionMixin, SuccessUrlKwargsMixin, UpdateView):
    prefix = 'goal'
    form_class = GoalForm
    model = Goal
    template_name = 'goals/goal_update_form.html'
    pk_url_kwarg = 'goal_pk'
    success_url_name = 'main:goal'
    url_kwargs = ['goal_pk']


class GoalDeleteView(GoalPermissionMixin, DeleteView):
    success_url = reverse_lazy('main:home')
    model = Goal
    template_name = 'goals/goal_confirm_delete.html'
    pk_url_kwarg = 'goal_pk'


# books views
class BookListView(BaseGoalChildListView):
    model = Book
    template_name = 'books/books.html'


class BookDetailView(BaseGoalChildDetailView):
    model = Book
    template_name = 'books/book.html'
    pk_url_kwarg = 'book_pk'


class BookCreateView(BaseGoalChildCreateView):
    success_url_name = 'main:books'
    url_kwargs = ['goal_pk']
    prefix = 'book'
    form_class = BookForm
    model = Book
    template_name = 'books/book_create_form.html'


class BookUpdateView(BaseGoalChildUpdateView):
    success_url_name = 'main:book'
    url_kwargs = ['goal_pk', 'book_pk']
    prefix = 'book'
    form_class = BookForm
    model = Book
    template_name = 'books/book_update_form.html'
    pk_url_kwarg = 'book_pk'


class BookDeleteView(BaseGoalChildDeleteView):
    success_url_name = 'main:books'
    url_kwargs = ['goal_pk']
    model = Book
    template_name = 'books/book_confirm_delete.html'
    pk_url_kwarg = 'book_pk'


# notes views
class NoteListView(BaseGoalChildListView):
    model = Note
    template_name = 'notes/notes.html'


class NoteDetailView(BaseGoalChildDetailView):
    model = Note
    template_name = 'notes/note.html'
    pk_url_kwarg = 'note_pk'


class NoteCreateView(BaseGoalChildCreateView):
    success_url_name = 'main:notes'
    url_kwargs = ['goal_pk']
    prefix = 'note'
    form_class = NoteForm
    model = Note
    template_name = 'notes/note_create_form.html'


class NoteUpdateView(BaseGoalChildUpdateView):
    success_url_name = 'main:note'
    url_kwargs = ['goal_pk', 'note_pk']
    prefix = 'note'
    form_class = NoteForm
    model = Note
    template_name = 'notes/note_update_form.html'
    pk_url_kwarg = 'note_pk'


class NoteDeleteView(BaseGoalChildDeleteView):
    success_url_name = 'main:notes'
    url_kwargs = ['goal_pk']
    model = Note
    template_name = 'notes/note_confirm_delete.html'
    pk_url_kwarg = 'note_pk'


# codes views
class CodeListView(BaseGoalChildListView):
    model = CodeExample
    template_name = 'codes/codes.html'


class CodeDetailView(BaseGoalChildDetailView):
    model = CodeExample
    template_name = 'codes/code.html'
    pk_url_kwarg = 'code_pk'


class CodeCreateView(BaseGoalChildCreateView):
    success_url_name = 'main:codes'
    url_kwargs = ['goal_pk']
    prefix = 'code'
    form_class = CodeExampleForm
    model = CodeExample
    template_name = 'codes/code_create_form.html'


class CodeUpdateView(BaseGoalChildUpdateView):
    success_url_name = 'main:code'
    url_kwargs = ['goal_pk', 'code_pk']
    prefix = 'code'
    form_class = CodeExampleForm
    model = CodeExample
    template_name = 'codes/code_update_form.html'
    pk_url_kwarg = 'code_pk'


class CodeDeleteView(BaseGoalChildDeleteView):
    success_url_name = 'main:codes'
    url_kwargs = ['goal_pk']
    model = CodeExample
    template_name = 'codes/code_confirm_delete.html'
    pk_url_kwarg = 'code_pk'


# tasks views
class TaskListView(BaseGoalChildListView):
    model = Task
    template_name = 'tasks/tasks.html'


class TaskDetailView(BaseGoalChildDetailView):
    model = Task
    template_name = 'tasks/task.html'
    pk_url_kwarg = 'task_pk'


class TaskCreateView(BaseGoalChildCreateView):
    success_url_name = 'main:tasks'
    url_kwargs = ['goal_pk']
    prefix = 'task'
    form_class = TaskForm
    model = Task
    template_name = 'tasks/task_create_form.html'


class TaskUpdateView(BaseGoalChildUpdateView):
    success_url_name = 'main:task'
    url_kwargs = ['goal_pk', 'task_pk']
    prefix = 'task'
    form_class = TaskForm
    model = Task
    template_name = 'tasks/task_update_form.html'
    pk_url_kwarg = 'task_pk'


class TaskDeleteView(BaseGoalChildDeleteView):
    success_url_name = 'main:tasks'
    url_kwargs = ['goal_pk']
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    pk_url_kwarg = 'task_pk'
