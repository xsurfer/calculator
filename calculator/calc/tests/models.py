from unittest import TestCase
from calc.models import Calculator


class CalculatorTestCase(TestCase):

    def setUp(self):
        super(CalculatorTestCase, self).setUp()
        self.calculator = Calculator()


    def test_add_op(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.expression, '')
        self.calculator.add_op(v=2,op='sum')
        self.assertEqual(self.calculator.expression, '2+')
        self.calculator.add_op(v=3,op='min')
        self.assertEqual(self.calculator.expression, '2+3-')
        self.calculator.add_op(v=15,op='mul')
        self.assertEqual(self.calculator.expression, '2+3-15*')
        self.calculator.add_op(v=2,op='div')
        self.assertEqual(self.calculator.expression, '2+3-15*2/')
        self.calculator.add_op(v=1)
        self.assertEqual(self.calculator.expression, '2+3-15*2/1')


    def test_evaluate(self):
        self.calculator = Calculator()
        self.assertEqual(self.calculator.expression, '')
        self.calculator.add_op(v=2,op='sum')
        self.assertEqual(self.calculator.expression, '2+')
        self.calculator.add_op(v=3,op='min')
        self.assertEqual(self.calculator.expression, '2+3-')
        self.calculator.add_op(v=15,op='mul')
        self.assertEqual(self.calculator.expression, '2+3-15*')
        self.calculator.add_op(v=2,op='div')
        self.assertEqual(self.calculator.expression, '2+3-15*2/')
        self.calculator.add_op(v=1)
        self.assertEqual(self.calculator.expression, '2+3-15*2/1')
        error, total = self.calculator.evaluate()
        self.assertEqual(error, 0)
        self.assertEqual(total, -25)

        #testing division by zero
        self.calculator = Calculator()
        self.assertEqual(self.calculator.expression, '')
        self.calculator.add_op(v=2,op='sum')
        self.assertEqual(self.calculator.expression, '2+')
        self.calculator.add_op(v=3,op='min')
        self.assertEqual(self.calculator.expression, '2+3-')
        self.calculator.add_op(v=15,op='mul')
        self.assertEqual(self.calculator.expression, '2+3-15*')
        self.calculator.add_op(v=2,op='div')
        self.assertEqual(self.calculator.expression, '2+3-15*2/')
        self.calculator.add_op(v=0)
        self.assertEqual(self.calculator.expression, '2+3-15*2/0')
        error, total = self.calculator.evaluate()
        self.assertEqual(error, 'Division/Modulo by zero')
        self.assertEqual(total, None)