from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden, Http404
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView, DetailView
from django.views.generic.detail import SingleObjectMixin

from syk.apps.main.models import Goal


class PermissionsMixin(object):
    def has_object_permission(self, request, obj):
        return True

    def get_permission_object(self):
        return self.get_object()

    def dispatch(self, request, *args, **kwargs):
        self.permission_object = self.get_permission_object()
        if not self.has_object_permission(request, self.object):
            return HttpResponseForbidden()
        super(PermissionsMixin, self).dispatch(request, *args, **kwargs)


class GoalPermissionMixin(PermissionsMixin):
    def get_permission_object(self):
        if self.object.__class__ is Goal:
            return self.object
        else:
            assert self.kwargs['goal_pk']
            try:
                return Goal.objects.get(pk=self.kwargs['goal_pk'])
            except ObjectDoesNotExist:
                raise Http404('Goal does not exist')

    def has_object_permission(self, request, obj):
        return self.permission_object.owner == request.user


class BaseGoalChildListView(ListView, GoalPermissionMixin):
    def get_queryset(self):
        if self.queryset is None:
            return self.model.objects.filter(goal=self.get_permission_object())
        else:
            return super(BaseGoalChildListView, self).get_queryset()


class BaseGoalChildDetailView(DetailView, GoalPermissionMixin):
    pass


class BaseGoalChildCreateView(CreateView, GoalPermissionMixin):
    def form_valid(self, form):
        form.instance.goal_id = self.kwargs['goal_pk']
        return super(BaseGoalChildCreateView, self).form_valid(form)


class BaseGoalChildUpdateView(UpdateView, GoalPermissionMixin):
    def dispatch(self, request, *args, **kwargs):
        self.success_url = reverse('main:goal', kwargs={'goal_pk': self.kwargs['goal_pk'],
                                                        self.pk_url_kwarg: self.kwargs[self.pk_url_kwarg]})
        return super(BaseGoalChildUpdateView, self).dispatch(request, *args, **kwargs)


class BaseGoalChildDeleteView(DeleteView, GoalPermissionMixin):
    pass
