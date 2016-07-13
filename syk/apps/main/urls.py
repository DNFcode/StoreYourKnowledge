from django.conf.urls import url, include
from views import GoalCreateView, GoalUpdateView, HomeView, GoalView, GoalDeleteView,\
    BookCreateView, BookDeleteView, BookDetailView, BookListView, BookUpdateView, \
    NoteCreateView, NoteDeleteView, NoteDetailView, NoteListView, NoteUpdateView, \
    CodeCreateView, CodeDeleteView, CodeDetailView, CodeListView, CodeUpdateView, \
    TaskCreateView, TaskDeleteView, TaskDetailView, TaskListView, TaskUpdateView
from django.views.generic import TemplateView

app_name = 'main'

tasks_pattern = [
    url(r'^tasks/$', TaskListView.as_view(), name='tasks'),
    url(r'^task/(?P<task_pk>\d+)$', TaskDetailView.as_view(), name='task'),
    url(r'^task/create$', TaskCreateView.as_view(), name='task-create'),
    url(r'^task/update/(?P<task_pk>\d+)$', TaskUpdateView.as_view(), name='task-update'),
    url(r'^task/delete/(?P<task_pk>\d+)$', TaskDeleteView.as_view(), name='task-delete'),
]

books_pattern = [
    url(r'^books/$', BookListView.as_view(), name='books'),
    url(r'^book/(?P<book_pk>\d+)$', BookDetailView.as_view(), name='book'),
    url(r'^book/create$', BookCreateView.as_view(), name='book-create'),
    url(r'^book/update/(?P<book_pk>\d+)$', BookUpdateView.as_view(), name='book-update'),
    url(r'^book/delete/(?P<book_pk>\d+)$', BookDeleteView.as_view(), name='book-delete'),
]

codes_pattern = [
    url(r'^codes/$', CodeListView.as_view(), name='codes'),
    url(r'^code/(?P<code_pk>\d+)$', CodeDetailView.as_view(), name='code'),
    url(r'^code/create$', CodeCreateView.as_view(), name='code-create'),
    url(r'^code/update/(?P<code_pk>\d+)$', CodeUpdateView.as_view(), name='code-update'),
    url(r'^code/delete/(?P<code_pk>\d+)$', CodeDeleteView.as_view(), name='code-delete'),
]

notes_pattern = [
    url(r'^notes/$', NoteListView.as_view(), name='notes'),
    url(r'^note/(?P<note_pk>\d+)$', NoteDetailView.as_view(), name='note'),
    url(r'^note/create$', NoteCreateView.as_view(), name='note-create'),
    url(r'^note/update/(?P<note_pk>\d+)$', NoteUpdateView.as_view(), name='note-update'),
    url(r'^note/delete/(?P<note_pk>\d+)$', NoteDeleteView.as_view(), name='note-delete'),
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

