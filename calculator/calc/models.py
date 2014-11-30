from django.db import models

# Create your models here.
class Calculator(models.Model):
    OPERATIONS = (
        ('sum', 'sum'),
        ('min', 'min'),
        ('mul', 'mul'),
        ('div', 'div'),
        ('equ', 'equ'),
    )
    valueA = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    valueB = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    operation = models.CharField(max_length=3, choices=OPERATIONS, )

    def evaluate(self):
        if self.operation == 'equ':
            return (float(self.valueA), None)
        elif self.operation == 'sum':
            return (float(self.valueA + self.valueB), None)
        elif self.operation == 'min':
            return (float(self.valueA - self.valueB), None)
        elif self.operation == 'mul':
            return (float(self.valueA * self.valueB), None)
        elif self.operation == 'div':
            if self.valueB == 0:
                print("Division by zero")
                return (None, 'Division by zero')
            return (float(self.valueA / self.valueB), None)
        return 0
