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
        if getattr(self, 'object', None).__class__ is Goal:
            return self.object
        else:
            assert self.kwargs['goal_pk']
            try:
                return Goal.objects.get(pk=self.kwargs['goal_pk'])
            except ObjectDoesNotExist:
                raise Http404('Goal does not exist')

    def has_object_permission(self, request, obj):
        return self.permission_object.owner == request.user


class SuccessUrlKwargsMixin(object):
    """
    A mixin that provides possibility to get 'success_url' by it's name and kwargs from request
    :arg `success_url_name`: urlpattern name
    :arg `url_kwarg`: list of kwargs from current request
    """
    success_url_name = None
    url_kwargs = None

    def get_success_url(self):
        if self.success_url_name:
            if self.url_kwargs:
                kwargs = {kwarg:self.kwargs.get(kwarg) for kwarg in self.url_kwargs}
                url = reverse(self.success_url_name, kwargs=kwargs)
            else:
                url = reverse(self.success_url_name)
        else:
            url = super(SuccessUrlKwargsMixin, self).get_success_url()
        return url


class BaseGoalChildListView(ListView, GoalPermissionMixin):
    def get_queryset(self):
        if self.queryset is None:
            return self.model.objects.filter(goal=self.get_permission_object())
        else:
            return super(BaseGoalChildListView, self).get_queryset()


class BaseGoalChildDetailView(DetailView, GoalPermissionMixin):
    pass


class BaseGoalChildCreateView(SuccessUrlKwargsMixin, CreateView, GoalPermissionMixin):
    def form_valid(self, form):
        form.instance.goal_id = self.kwargs['goal_pk']
        return super(BaseGoalChildCreateView, self).form_valid(form)


class BaseGoalChildUpdateView(SuccessUrlKwargsMixin, UpdateView, GoalPermissionMixin):
    pass


class BaseGoalChildDeleteView(SuccessUrlKwargsMixin, DeleteView, GoalPermissionMixin):
    pass
