from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseForbidden, Http404
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.detail import SingleObjectMixin

from syk.apps.main.forms import GoalForm
from syk.apps.main.models import Goal, Book


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


class BaseGoalChildObjectView(SingleObjectMixin, TemplateView, GoalPermissionMixin):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(BaseGoalChildObjectView, self).get(request, *args, **kwargs)