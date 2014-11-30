from django.http import HttpResponse

# Create your views here.
from django.template import RequestContext, loader

# def index(request):
# init = request.GET.get('init',True)
# print('init: %s' % init)
#
#     currVal = float( request.GET.get('input',0) )
#     print('curVal: %s' % currVal)
#
#     op = request.GET.get('op',None)
#     print('op: %s' % op)
#
#     if init is False:
#         showTotal=True
#         showCurr=True
#     else:
#         showTotal=False
#         showCurr=False
#
#     total = 0
#
#     template = loader.get_template('index.html')
#     context = RequestContext(request, {
#         'init': init,
#         'showTotal': showTotal,
#         'total': str(total),
#         'showTotal': showCurr,
#         'curr' : str(currVal),
#         'op' : op,
#     })
#     return HttpResponse(template.render(context))
#
from forms import CalculatorForm


def index2(request):
    step = request.GET.get('step', '1')
    currVal = float(request.GET.get('input', 0))
    print(currVal)
    currOp = request.GET.get('op', None)
    print(currOp)
    total = 0

    print('step: %s' % step)
    if step == '1':  # show just the buttons w/o any label
        showVal = False
        showTotal = False
        request.session['preVal'] = 0
        step = 2
    elif step == '2':  # show selected value and op ... waiting for the second value
        showVal = True
        showTotal = False
        request.session['preVal'] = currVal
        request.session['op'] = currOp
        step = 3
    elif step == '3':  # show previous value, op and total; if operation not 'equals' then allows user to digit new value
        showVal = True
        showTotal = True
        total = doOp(request.session['op'], float(request.session['preVal']), currVal)
        if currOp == 'eq':
            step = 0
            showVal = False
            showTotal = True
            print("finished")
        else:
            step = 3
            request.session['preVal'] = total
            request.session['op'] = currOp

    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'step': step,
        'showVal': showVal,
        'val': currVal,
        'op': currOp,
        'showTotal': showTotal,
        'total': total

    })
    return HttpResponse(template.render(context))


def index(request):
    total=None
    step=None
    error=None
    form=None

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CalculatorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            step=form.cleaned_data['step']
            input=float(form.cleaned_data['input'])
            op= form.cleaned_data['op']
            step, total, error = validForm(request, step, input, op)
    else:
        # initialize variables
        step, total, error = reset(request)


    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'form' : form,
        'error': error,
        'total': total,
        'step': step,
        })
    return HttpResponse(template.render(context))


def validForm(request, step, input, op):
    error=None
    if op == 'clc':
        step, total, error = reset(request)
    elif op == 'equ':
        if request.session['op'] and request.session['preVal']:
            total, error = doOp(request.session['op'], request.session['preVal'], float(input))
        else:
            total = input
        step=1
    else:
        if step == 1:      # no total
            request.session['preVal'] = float(input)
            request.session['op'] = op
            total=None
            step=2
        elif step == 2:    # there is total
            total,  error = doOp(request.session['op'], request.session['preVal'], input)
            request.session['preVal'] = total
            if op != 'equ':
                request.session['op'] = op
            step=2
    return (step, total, error)


def reset(request):
    error=None
    total=None
    step=1
    request.session['preVal'] = float(0)
    request.session['op'] = None
    return (step, total, error)



def doOp(op, a, b):
    print("operating...")
    if op == 'sum':
        return (a + b, None)
    elif op == 'min':
        return (a - b, None)
    elif op == 'mul':
        return (a * b, None)
    elif op == 'div':
        if b==0:
            print("Division by zero")
            return (None, 'Division by zero')
        return (float(a / b), None)
    return 0


