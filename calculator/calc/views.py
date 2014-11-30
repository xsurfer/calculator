from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import RequestContext, loader

# def index(request):
#     init = request.GET.get('init',True)
#     print('init: %s' % init)
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


def index(request):
    step = request.GET.get('step','1')
    currVal = float( request.GET.get('input',0) )
    print(currVal)
    currOp = request.GET.get('op',None)
    print(currOp)
    total = 0

    print('step: %s' % step)
    if step == '1': # non visualizzare nulla
        showVal=False
        showTotal=False
        request.session['preVal'] = 0
        step = 2
    elif step == '2': # visualizzare valore e operazione, in attesa dell'altro valore
        showVal=True
        showTotal=False
        request.session['preVal'] = currVal
        request.session['op'] = currOp
        step = 3
    elif step == '3':   # visualizzare valore, operazione e totale temporaneo, in attesa di altro valore
        showVal=True
        showTotal=True
        total = doOp( request.session['op'], float(request.session['preVal']), currVal )
        if currOp == 'eq':
            step = 0
        else:
            step = 3
            request.session['preVal'] = total
            request.session['op'] = currOp
    elif step == '0':   # visualizzare totale
        showVal=False
        showTotal=True

    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'step' : step,
        'showVal': showVal,
        'val' : currVal,
        'op' : currOp,
        'showTotal' : showTotal,
        'total' : total

    })
    return HttpResponse(template.render(context))

def doOp(op, a, b):
    if op == 'sum':
        return a+b
    elif op == 'minus':
        return a-b
    elif op == 'mult':
        return a*b
    elif op == 'div':
        return a/b
    return 0


