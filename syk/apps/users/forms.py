import django.contrib.auth.forms as auth_forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FormActions


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        fields = ("username", "first_name", "last_name", "email")

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-4'
    helper.field_class = 'col-lg-8'
    helper.layout = Layout(
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2',
        FormActions(
                Submit('submit', 'Create account')
        )
    )


class UserAuthForm(auth_forms.AuthenticationForm):
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-4'
    helper.field_class = 'col-lg-8'
    helper.layout = Layout(
        'username',
        'password',
        FormActions(
                Submit('submit', 'Log in')
        )
    )