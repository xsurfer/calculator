from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import RequestContext, loader

def index(request):
    init = request.GET.get('init',True)
    print('init: %s' % init)

    currVal = float( request.GET.get('input',0) )
    print('curVal: %s' % currVal)

    op = request.GET.get('op',None)
    print('op: %s' % op)

    if init is False:
        showTotal=True
        showCurr=True
    else:
        showTotal=False
        showCurr=False

    total = 0

    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'init': init,
        'showTotal': showTotal,
        'total': str(total),
        'showTotal': showCurr,
        'curr' : str(currVal),
        'op' : op,
    })
    return HttpResponse(template.render(context))
