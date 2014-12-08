import logging
from django.http import HttpResponse

# Create your views here.
from django.template import RequestContext, loader
from models import Calculator
from forms import CalculatorForm

logger = logging.getLogger(__name__)

def index(request):
    error=None
    total=None
    form=None
    expression=None
    if request.method == 'POST':
        calculator=Calculator.objects.get(pk = request.session['calculator'])
        logger.debug("Calculator id: %d" % calculator.pk)
        form = CalculatorForm(request.POST)
        if form.is_valid():
            logger.debug("Form is valid")
            op = form.cleaned_data['op']
            value = form.cleaned_data['input']
            if op == 'equ':
                calculator.add_op(v=value)
                error, total = calculator.evaluate()
                logger.debug("error: %s" % error)
                logger.debug("total: %s" % total)
                reset(request)
            elif op == 'clc':
                reset(request)
            else:
                calculator.add_op(v=value, op=op)
            expression= calculator.expression
            calculator.save()
        else:
            logger.debug("Not valid form")
            pass
    else:
        logger.debug("Not post action")
        reset(request)


    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'expression' : expression,
        'form': form,
        'error': error,
        'total': total,
        })
    return HttpResponse(template.render(context))


def reset(request):
    calculator=Calculator()
    calculator.save()
    request.session['calculator'] = calculator.pk
    logger.debug("Calculator id: %d" % calculator.pk)


