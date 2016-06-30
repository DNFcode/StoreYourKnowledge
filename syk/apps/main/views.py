from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.detail import SingleObjectMixin

from forms import GoalForm, BookForm
from models import Goal, Book
from syk.apps.main.views_utils import GoalPermissionMixin
from syk.apps.main.views_utils import BaseGoalChildCreateView, BaseGoalChildDeleteView, BaseGoalChildObjectView, BaseGoalChildUpdateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_goals(self):
        return Goal.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        kwargs['goals'] = self.get_goals()
        return super(HomeView, self).get_context_data(**kwargs)


# goals
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


class GoalView(SingleObjectMixin, TemplateView, GoalPermissionMixin):
    template_name = 'goal.html'
    model = Goal
    object = None
    pk_url_kwarg = 'goal_pk'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(GoalView, self).get(request, *args, **kwargs)


# books
class BookCreateView(BaseGoalChildCreateView):
    prefix = 'book'
    form_class = BookForm
    model = Book
    template_name = "book_create_form.html"