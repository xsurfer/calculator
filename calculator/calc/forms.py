import logging

from django import forms

from models import Calculator


logger = logging.getLogger(__name__)


class CalculatorForm(forms.Form):
    input = forms.DecimalField(label='', max_digits=999, decimal_places=4, required=False)
    op = forms.ChoiceField(choices=Calculator.OPERATIONS, required=True)


    def clean(self):
        cleaned_data = super(CalculatorForm, self).clean()
        op = cleaned_data.get("op")
        input = cleaned_data.get("input")
        if op != 'clc' and input == None:
            logger.debug("validation check")
            raise forms.ValidationError("Required field.")
            # return cleaned_data