from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from forms import GoalForm, BookForm
from models import Goal, Book
from syk.apps.main.views_utils import GoalPermissionMixin
from syk.apps.main.views_utils import BaseGoalChildCreateView, BaseGoalChildDeleteView, BaseGoalChildUpdateView, \
    BaseGoalChildListView, BaseGoalChildDetailView


# goals views
class HomeView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        if self.queryset is None:
            return Goal.objects.filter(owner=self.request.user)
        else:
            return super(HomeView, self).get_queryset()


class GoalView(DetailView, GoalPermissionMixin):
    template_name = 'goal.html'
    model = Goal
    pk_url_kwarg = 'goal_pk'


class GoalCreateView(CreateView):
    success_url = reverse_lazy('main:home')
    prefix = 'goal'
    form_class = GoalForm
    model = Goal
    template_name = 'goal_create_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(GoalCreateView, self).form_valid(form)


class GoalUpdateView(UpdateView, GoalPermissionMixin):
    prefix = 'goal'
    form_class = GoalForm
    model = Goal
    template_name = 'goal_update_form.html'
    pk_url_kwarg = 'goal_pk'

    def dispatch(self, request, *args, **kwargs):
        self.success_url = reverse('main:goal', kwargs={'goal_pk': self.kwargs['goal_pk']})
        return super(GoalUpdateView, self).dispatch(request, *args, **kwargs)


class GoalDeleteView(DeleteView, GoalPermissionMixin):
    success_url = reverse_lazy('main:home')
    model = Goal
    template_name = 'goal_confirm_delete.html'
    pk_url_kwarg = 'goal_pk'


# books views
class BookListView(BaseGoalChildListView):
    model = Book
    template_name = 'books.html'


class BookDetailView(BaseGoalChildDetailView):
    model = Book
    template_name = 'book.html'
    pk_url_kwarg = 'book_pk'


class BookCreateView(BaseGoalChildCreateView):
    success_url_name = 'main:books'
    url_kwargs = ['goal_pk']
    prefix = 'book'
    form_class = BookForm
    model = Book
    template_name = 'book_create_form.html'


class BookUpdateView(BaseGoalChildUpdateView):
    success_url_name = 'main:book'
    url_kwargs = ['goal_pk', 'book_pk']
    prefix = 'book'
    form_class = BookForm
    model = Book
    template_name = 'book_update_form.html'
    pk_url_kwarg = 'book_pk'


class BookDeleteView(BaseGoalChildDeleteView):
    success_url_name = 'main:books'
    url_kwargs = ['goal_pk']
    model = Book
    template_name = 'book_confirm_delete.html'
    pk_url_kwarg = 'book_pk'


# notes views
