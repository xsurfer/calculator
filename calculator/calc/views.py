from django.http import HttpResponse

# Create your views here.
from django.template import RequestContext, loader
from models import Calculator
from forms import CalculatorForm


def index(request):
    total = None
    step = None
    error = None
    form = None

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CalculatorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # retrieving data
            print("Form is Valid")
            step = form.cleaned_data['step']
            input = float(form.cleaned_data['input'])
            op = form.cleaned_data['op']
            step, total, error = validForm(request, step, input, op)
    else:
        # initialize variables
        step, total, error = reset(request)

    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'form': form,
        'error': error,
        'total': total,
        'step': step,
        })
    return HttpResponse(template.render(context))


def reset(request):
    error = None
    total = None
    step = 1
    request.session['calculator'] = None
    return (step, total, error)


def validForm(request, step, input, op):
    error = None
    total = None
    if op == 'clc':
        request.session['calculator'] = None
        total = None
        step = 1
    elif step == 1:
        if op == 'equ':
            calc = Calculator(valueA=float(input), operation=op)
            total = calc.evaluate()
            step = 1
        else:
            request.session['valueA'] = input
            request.session['operation'] = op
            step = 2
    elif step == 2:
        if op == 'equ':
            valueA = request.session.get('valueA', 0)
            op = request.session['operation']
            calc = Calculator(valueA=float(valueA), valueB=float(input), operation=op)
            total, error = calc.evaluate()
            request.session['valueA'] = total
            print(total)
            step = 1
        else:
            op = request.session['operation']
            valueA = request.session['valueA']
            calc = Calculator(valueA=float(valueA), valueB=float(input), operation=op)
            total, error = calc.evaluate()
            request.session['valueA'] = total
            request.session['operation'] = op
            print(total)
            step = 2
    return (step, total, error)


