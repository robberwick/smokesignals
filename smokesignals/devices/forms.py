from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button
from crispy_forms.bootstrap import FormActions
from .models import Device


class DeviceUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeviceUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'id',
            'title',
            FormActions(
                Submit('save', 'Save changes'),
                Button('cancel', 'Cancel')
            )
        )

    class Meta:
        # Set this form to use the Device model.
        model = Device

        # Constrain the UserForm to just these fields.
        fields = ["id", "title"]


class DeviceCreateForm(DeviceUpdateForm):
    def __init__(self, *args, **kwargs):
        super(DeviceCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Device
        fields = ['title', ]
