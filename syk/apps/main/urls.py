from django.conf.urls import url, include
from views import GoalCreateView, GoalUpdateView, HomeView, GoalView, GoalDeleteView,\
    BookCreateView, BookDeleteView, BookDetailView, BookListView, BookUpdateView
from django.views.generic import TemplateView

app_name = 'main'

tasks_pattern = [
    url(r'^tasks/$', TemplateView.as_view(template_name="tasks.html"), name='tasks'),
    # url(r'^task/(?P<task_pk>\d+)$', View.as_view(), name='task'),
    # url(r'^task/create$', View.as_view(), name='task-create'),
    # url(r'^task/update/(?P<task_pk>\d+)$', View.as_view(), name='task-update'),
    # url(r'^task/delete/(?P<task_pk>\d+)$', View.as_view(), name='task-delete'),
]

books_pattern = [
    url(r'^books/$', BookListView.as_view(template_name="books.html"), name='books'),
    url(r'^book/(?P<book_pk>\d+)$', BookDetailView.as_view(), name='book'),
    url(r'^book/create$', BookCreateView.as_view(), name='book-create'),
    url(r'^book/update/(?P<book_pk>\d+)$', BookUpdateView.as_view(), name='book-update'),
    url(r'^book/delete/(?P<book_pk>\d+)$', BookDeleteView.as_view(), name='book-delete'),
]

codes_pattern = [
    # url(r'^codes/$', TemplateView.as_view(template_name="codes.html"), name='codes'),
    # url(r'^code/(?P<code_pk>\d+)$', View.as_view(), name='code'),
    # url(r'^code/create$', View.as_view(), name='code-create'),
    # url(r'^code/update/(?P<code_pk>\d+)$', View.as_view(), name='code-update'),
    # url(r'^code/delete/(?P<code_pk>\d+)$', View.as_view(), name='code-delete'),
]

notes_pattern = [
    # url(r'^notes/$', TemplateView.as_view(template_name="notes.html"), name='notes'),
    # url(r'^note/(?P<note_pk>\d+)$', View.as_view(), name='note'),
    # url(r'^note/create$', View.as_view(), name='note-create'),
    # url(r'^note/update/(?P<note_pk>\d+)$', View.as_view(), name='note-update'),
    # url(r'^note/delete/(?P<note_pk>\d+)$', View.as_view(), name='note-delete'),
]

urlpatterns = [
    url(r'^home/$', HomeView.as_view(), name='home'),

    # goals
    url(r'^goal/(?P<goal_pk>\d+)$', GoalView.as_view(), name='goal'),
    url(r'^goal/create$', GoalCreateView.as_view(), name='goal-create'),
    url(r'^goal/update/(?P<goal_pk>\d+)$', GoalUpdateView.as_view(), name='goal-update'),
    url(r'^goal/delete/(?P<goal_pk>\d+)$', GoalDeleteView.as_view(), name='goal-delete'),

    url(r'^goal/(?P<goal_pk>\d+)/', include(tasks_pattern + books_pattern + notes_pattern + codes_pattern)),
]

