from django import forms

OPERATIONS = (
    ('sum', 'sum'),
    ('min', 'min'),
    ('mul', 'mul'),
    ('div', 'div'),
    ('equ', 'equ'),
    ('clc', 'clc'),
)

class CalculatorForm(forms.Form):
    input = forms.DecimalField(label='', max_digits = 10, decimal_places=3, required=True)
    op = forms.ChoiceField(choices=OPERATIONS, required=True)
    step = forms.IntegerField(required=True)