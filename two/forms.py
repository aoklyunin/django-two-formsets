from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.forms import ModelForm, TextInput
from django_select2.forms import Select2Widget

from two.models import Equipment, MoveEquipment


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = {'name', 'dimension', 'code'}
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Перчатки'}),
            'dimension': TextInput(attrs={'placeholder': 'пара'}),
        }

        labels = {
            'name': 'Название',
            'dimension': 'Единица измерения',
            'code': 'Шифр',
        }

        error_messages = {
            'name': {'invalid': '', 'invalid_choice': ''},
            'dimension': {'required': ''},
        }

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(EquipmentForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['dimension'].required = False
        self.fields['code'].required = False
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name', css_class='col-sm-2', ),
            Field('dimension', css_class='col-sm-2'),
            Field('code', css_class='col-sm-2'),

        )


class MoveForm(ModelForm):
    class Meta:
        model = MoveEquipment
        fields = {'cnt', 'equipment'}
        widgets = {
        }

        labels = {
            'equipment': '',
            'cnt': '',
        }

        error_messages = {
            'equipment': {'invalid': '', 'invalid_choice': ''},
            'cnt': {'required': ''},
        }

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(MoveForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['equipment'].required = False
        self.fields['cnt'].required = False

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('cnt', css_class='col-sm-2', ),
            Field('equipment', css_class='col-sm-2'))


class MoveEquipmentForm(MoveForm):
    def __init__(self, *args, **kwargs):
        super(MoveEquipmentForm, self).__init__(*args, **kwargs)
        self.fields['equipment'].queryset = Equipment.objects.filter(equipmentType=Equipment.TYPE_EQUIPMENT)


class MoveMaterialForm(MoveForm):
    def __init__(self, *args, **kwargs):
        super(MoveMaterialForm, self).__init__(*args, **kwargs)
        self.fields['equipment'].queryset = Equipment.objects.filter(equipmentType=Equipment.TYPE_MATERIAL)


class MoveDetailForm(MoveForm):
    def __init__(self, *args, **kwargs):
        super(MoveDetailForm, self).__init__(*args, **kwargs)
        self.fields['equipment'].queryset = Equipment.objects.filter(equipmentType=Equipment.TYPE_DETAIL)


class MoveAssemblyForm(MoveForm):
    def __init__(self, *args, **kwargs):
        super(MoveAssemblyForm, self).__init__(*args, **kwargs)
        self.fields['equipment'].queryset = Equipment.objects.filter(equipmentType=Equipment.TYPE_ASSEMBLY_UNIT)


class MoveStandartWorkForm(MoveForm):
    def __init__(self, *args, **kwargs):
        super(MoveStandartWorkForm, self).__init__(*args, **kwargs)
        self.fields['equipment'].queryset = Equipment.objects.filter(equipmentType=Equipment.TYPE_STANDART_WORK)