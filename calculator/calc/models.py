import logging
from decimal import Decimal
from django.db import models


logger = logging.getLogger(__name__)


class Calculator(models.Model):

    ERRORS = (
        (0,'No errors'),
        (1,'Division/Modulo by zero'),
    )

    OPERATIONS = (
        ('sum','+'),
        ('min','-'),
        ('mul','*'),
        ('div','/'),
        ('equ','='),
        ('clc','#'),
    )
    expression = models.CharField(max_length=100, default='')

    def add_op(self, v, op=None):
        if self.expression is None:
            self.expression = ''
        self.expression += str(float(v))
        if op:
            self.expression += str( dict(self.OPERATIONS)[op])
        logger.debug("expression: %s" % self.expression)
        return self.expression


    def evaluate(self):
        logger.debug("expression: %s" % self.expression)
        try:
            return (0, eval((str(self.expression))))
        except ZeroDivisionError:
            return (dict(self.ERRORS)[1], None)