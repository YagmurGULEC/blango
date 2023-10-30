from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_registration.forms import RegistrationForm

from .models import CustomUser


class BlangoRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser

    # def __init__(self, *args, **kwargs):
    #     super(BlangoRegistrationForm, self).__init__(*args,
    #                                                  **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.add_input(Submit("submit", "Register"))
