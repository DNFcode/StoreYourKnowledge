from django.forms import ModelForm, Form
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from models import Goal, Book, Note, CodeExample, Task


class CrispyMixin(object):
    def __init__(self):
        super(CrispyMixin, self).__init__()
        self.layout = Layout(*self.Meta.fields)

    helper = FormHelper()
    helper.form_tag = False
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'


class GoalForm(ModelForm, CrispyMixin):
    class Meta:
        model = Goal
        fields = ['name', 'description']


class BookForm(ModelForm, CrispyMixin):
    class Meta:
        model = Book
        fields = ['name', 'description', 'pages']


class NoteForm(ModelForm, CrispyMixin):
    class Meta:
        model = Note
        fields = ['title', 'text']


class CodeExampleForm(ModelForm, CrispyMixin):
    class Meta:
        model = CodeExample
        fields = ['title', 'description', 'code']